from bottle import error, request, route, run, template
import json
from random import randint
import requests
import socket


HOSTNAME = socket.gethostname()
#hostname = '0.0.0.0'
HOSTPORT = 8080
ENDPOINT = 'http://wordtools-api:8081'  # api layer host/port set in compose file

# global variables representing state for the HTML template
# to do: put these into a dictionary - in fact, consider using the word_packet dict
last_anag = 'listen'
last_search = 'am_s_ng'
last_random = '10'
last_wordlen = '5'
last_rndrows = '10'
last_pswd = '3'
status = ''


def process_word_packet(word_packet):
    if word_packet['status'] > 0:
        body = word_packet['message'].split()
    else:
        body = word_packet['words']
    return body


def writebody(output):
    return template('base', hostname=HOSTNAME, output=output, anagram=last_anag, \
        search=last_search, random=last_random, wordlen=last_wordlen, rndrows=last_rndrows, \
        pswd=last_pswd)


@route('/')
def root():
    return writebody(None)


@route('/anagram', method='POST')
def anagram():
    global last_anag
    anagram = request.forms.get('anagram').lower()
    uri = '/anagram/' + anagram
    status = ' URI = ' + uri
    word_packet = requests.get(ENDPOINT + uri).json()
    body = process_word_packet(word_packet)
    last_anag = anagram
    return writebody(body)


@route('/finder', method='POST')
def finder():
    global last_search
    partial = request.forms.get('partial')
    uri = '/finder/' + partial
    status = ' URI = ' + uri
    word_packet = requests.get(ENDPOINT + uri).text
    body = process_word_packet(json.loads(word_packet))
    last_search = partial
    return writebody(body)


# generate a set of memorable passwords
@route('/pswd', method='POST')
def random():
    global last_pswd
    numberstr = request.forms.get('num')
    word_packet = {'words': [], 'count': 0, 'status': 0}
    for i in range(int(numberstr)):
        passphrase = ''
        for j in range(3):
            # get 1 word between 3 and 7 chars
            wordlen = randint(3, 7)
            uri = '/rnd/' + 1 + '/' + wordlen
            data_packet = requests.get(ENDPOINT + uri).json()
            # add a seperator to the words - To do: make seperator random char, or nothing
            passphrase += data_packet['words'][0] + ','
        # add a random number to the string
        passphrase += str(randint(9999))
        word_packet['words'].append(passphrase)
        word_packet['count'] += 1
    body = process_word_packet(word_packet)
    last_pswd = numberstr
    return writebody(body)


# serve random words of any length
@route('/random', method='POST')
def random():
    global last_random
    numberstr = request.forms.get('num')
    uri = '/random/' + numberstr
    word_packet = requests.get(ENDPOINT + uri).json()
    body = process_word_packet(word_packet)
    last_random = numberstr
    return writebody(body)


# serve random words of fixed length
@route('/rnd', method='POST')
def rnd():
    global last_wordlen
    global last_rndrows
    wordlen = request.forms.get('wordlen')
    numberstr = request.forms.get('num')
    uri = '/rnd/' + numberstr + '/' + wordlen
    word_packet = requests.get(ENDPOINT + uri).json()
    body = process_word_packet(word_packet)
    last_wordlen = wordlen
    last_rndrows = numberstr
    return writebody(body)


# simple test of presentation container
@route('/test')
def test():
    return '<h1>Presentation layer operational</h1>'


# simple test of API container
@route('/apitest')
def apitest():
    word_packet = requests.get(ENDPOINT + '/test').json()
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
run(host=HOSTNAME, port=HOSTPORT)
