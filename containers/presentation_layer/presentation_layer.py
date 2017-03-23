from bottle import error, request, route, run, template
import json
import requests
import socket

hostname = socket.gethostname()
#hostname = '0.0.0.0'
hostport = 8080
endpoint = 'http://localhost:8081'


def writebody(output):
    return template('base', hostname=hostname, output=output)


@route('/')
def root():
    return writebody(None)


@route('/anagram', method='POST')
def anagram():
    anagram = request.forms.get('anagram').lower()
    uri = '/anagram/' + anagram
    word_packet = requests.get(endpoint + uri).json()
    body_str = ''
    for word in word_packet['words']:
        body_str += word + ' '
    return writebody(body_str)


@route('/finder', method='POST')
def finder():
    partial = request.forms.get('partial')
    uri = '/finder/' + partial
    word_packet = requests.get(endpoint + uri).json()
    body_str = ''
    for word in word_packet['words']:
        body_str += word + ' '
    return writebody(body_str)


@route('/random', method='POST')
def random():
    numberstr = request.forms.get('num')
    uri = '/random/' + numberstr
    word_packet = requests.get(endpoint + uri).json()
    body_str = ''
    for word in word_packet['words']:
        body_str += word + ' '
    return writebody(body_str)


# simple test of layer connectivity
@route('/test')
def test():
    response = requests.get(endpoint + '/test')
    return response


@error(404)
def mistake404(code):
    return 'Sorry mate, path not found'


@error(405)
def mistake405(code):
    return 'Invalid arguments to form'


run(host=hostname, port=hostport)
