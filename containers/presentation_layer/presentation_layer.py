from bottle import error, request, route, run, template
import json
import requests
import socket


hostname = socket.gethostname()
#hostname = '0.0.0.0'
hostport = 8080
endpoint = 'http://wordtools-api:8081'  # api layer host/port set in compose file

last_anag = 'listen'
last_search = 'am_s_ng'
last_random = '10'
status = ''


def process_word_packet(word_packet):
    if word_packet['status'] > 0:
        body = word_packet['message'].split()
    else:
        body = word_packet['words']
    return body


def writebody(output):
    return template('base', hostname=hostname, output=output, anagram=last_anag, search=last_search, random=last_random)


@route('/')
def root():
    return writebody(None)


@route('/anagram', method='POST')
def anagram():
    global last_anag
    anagram = request.forms.get('anagram').lower()
    uri = '/anagram/' + anagram
    status = ' URI = ' + uri
    word_packet = requests.get(endpoint + uri).json()
    body = process_word_packet(word_packet)
    last_anag = anagram
    return writebody(body)


@route('/finder', method='POST')
def finder():
    global last_search
    partial = request.forms.get('partial')
    uri = '/finder/' + partial
    status = ' URI = ' + uri
    word_packet = requests.get(endpoint + uri).text
    body = process_word_packet(json.loads(word_packet))
    last_search = partial
    return writebody(body)


@route('/random', method='POST')
def random():
    global last_random
    numberstr = request.forms.get('num')
    uri = '/random/' + numberstr
    word_packet = requests.get(endpoint + uri).json()
    body = process_word_packet(word_packet)
    last_random = numberstr
    return writebody(body)

@route('/randomfixed', method='POST')
def randomfixed():
    wordlen = request.forms.get('wordlen')
    uri = '/randomfixed/' + wordlen
    word_packet = requests.get(endpoint + uri).json()
    body = process_word_packet(word_packet)
    return writebody(body)


# simple test of presentation container
@route('/test')
def test():
    return '<h1>Presentation layer operational</h1>'


# simple test of API container
@route('/apitest')
def apitest():
    word_packet = requests.get(endpoint + '/test').json()
    return word_packet['words']


@error(404)
def mistake404(code):
    return 'Sorry mate, 404 - path not found.'


@error(405)
def mistake405(code):
    return '405 - Invalid arguments to form.'

'''
@error(500)
def mistake500(code):
    return '500 - Returning error from presentation layer.' + status
'''
run(host=hostname, port=hostport)
