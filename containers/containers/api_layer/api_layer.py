from bottle import error, get, response, route, run
import json
import os
import pymysql
from random import randint
import socket
import sys

#hostname = socket.gethostname()
hostname = '0.0.0.0'
dbhost = 'wordtools-data' # name of the database server container, linked by compose file
hostport = 8081
max_words = 200

# dbpasswd = os.environ['MYSQL_PASSWORD']
dbpasswd = os.environ['MYSQL_PASSWORD']
dbuser = os.environ['MYSQL_USER']


def db_init():
    db = pymysql.connect(host=dbhost, db='worddb', user=dbuser, passwd=dbpasswd)
    return db


def set_headers():
    response.headers['Content-Type'] = 'application/json'
    response.headers['Cache-Control'] = 'no-cache'


# fetch a single row and return cursor
def single_row_query(db, query):
    try:
        with db.cursor() as cursor:
            cursor.execute(query)
            row_data = cursor.fetchone()[0]
    except Exception as e:
        print('Exception in single row query: ' + str(e))
        return None
    return row_data


# fetch multiple rows and return JSON output object
def multi_row_query(db, query):
    output = {'words': [], 'count': 0, 'status': 0}
    try:
        with db.cursor() as cursor:
            cursor.execute(query)
            # first check how many words come back
            if cursor.rowcount > max_words:
                output['status'] = 5
                output['message'] = 'Exceeded max words limit (' + str(max_words) + ')'
                return output
            if cursor.rowcount < 1:
                output['status'] = 6
                output['message'] = 'No words returned'
                return output
            words = cursor.fetchall()
            for word in words:
                output['count'] += 1
                output['words'].append(word[0])

    except Exception as e:
        output['status'] = 7
        output['message'] = str(e)
    return output


@get('/anagram/<source_word:re:[a-zA-Z]+>')
def anagram(source_word):
    set_headers()

    # get words of same length which contain at least all the same letters
    query = 'SELECT DISTINCT word FROM words WHERE '
    for letter in source_word:
        query += "word LIKE '%" + letter + "%' AND "
    query += "length = " + str(len(source_word))
    db = db_init()
    output = multi_row_query(db, query)
    db.close()
    sorted_word = sorted(source_word)

    # now filter out non-anagrams from the list (can happen if there were
    # double letters)
    new_output = []
    for word in output['words']:
        if sorted_word == sorted(word):
            new_output.append(word)
    output['words'] = new_output
    output['count'] = len(new_output)
    return output


# word search - to do: use a mask to limit characters
@get('/finder/<partial_word:re:[a-zA-Z_%]+>')
def finder(partial_word):
    set_headers()
    query = "SELECT word FROM words WHERE word LIKE '" + partial_word + "'"
    db = db_init()
    output = multi_row_query(db, query)
    db.close()
    return output


# returns random fixed length words
@get('/rnd/<num_words:int>/<length:int>')
def randomfixed(num_words, length):
    set_headers()

    db = db_init()
    query = 'SELECT word FROM words WHERE length = ' + str(length) + ' order by rand() limit ' \
        + str(num_words)
    output = multi_row_query(db, query)
    db.close()
    return output

# returns any random words
@get('/random/<num_words:int>')
def random(num_words):
    set_headers()
    output = {'words': [], 'count': 0, 'status': 0}

    if num_words > max_words:
        output['status'] = 8
        output['message'] = 'Exceeded max words limit (' + str(max_words) + ')'
        return output

    db = db_init()

    # count how many rows
    query = 'SELECT count(word) FROM words;'
    numrows = single_row_query(db, query)
    if numrows is None or numrows < 1:
        output['status'] = 9
        output['message'] = 'Empty table or database connectivity error'
    else:
        int_set = '('
        # build a set of random numbers between 1 and numrows
        for x in range(num_words):
            random_int = randint(1, numrows)
            int_set += str(random_int) + ','
        int_set = int_set[:-1] + ')'

        # query words matching the random row numbers
        query = 'SELECT word FROM words WHERE word_id IN ' + int_set

    output = multi_row_query(db, query)
    db.close()
    return output


# simple test of layer connectivity
@route('/test')
def test():
    output = {'words': ['API layer test successful'], 'count': 1, 'status': 0}
    return output


@error(404)
def mistake404(code):
    output = {'words': ['404 Sorry mate path not found'], 'count': 1, 'status': 1,
              'message': '404 Sorry mate path not found'}
    return output


@error(405)
def mistake405(code):
    output = {'words': ['405 Invalid arguments'], 'count': 1, 'status': 2,
              'message': '405 Invalid arguments'}
    return output


@error(500)
def mistake500(code):
    output = {'words': ['500 Internal Server Error'], 'count': 1, 'status': 3,
              'message': '500 Internal Server Error'}
    return output


run(host=hostname, port=hostport)
