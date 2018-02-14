'''Random word tool - display random dictionary words'''

import argparse
import random
import sys

# defaults
COUNT = 3
MINLEN = 3
WORDFILE = 'words.txt'

'''loads a line seperated word file into an array'''
def load_words(wordfile, minlen, maxlen):
    wordlist = []
    try:
        with open(wordfile) as wf:
            for word in wf:
                wordlen = len(word) - 1 # remove linefeed from word
                if wordlen >= minlen and (maxlen is None or wordlen <= maxlen):
                    wordlist.append(word[:-1])
    except FileNotFoundError:
        sys.exit('Error: cannot open file ' + wordfile)
    return wordlist


'''returns a set of count random ints between 0 and < len'''
def random_indexes(count, num_words):
    index_array = []
    for _ in range(count):
        random_num = random.randint(0, num_words - 1)
        index_array.append(random_num)
    return index_array


def main():
    '''Main routine.'''
    # validate command line arguments
    arg_parser = argparse.ArgumentParser()

    arg_parser.add_argument(
        '--count', '-n', action='store', type = int, help='Number of words')
    arg_parser.add_argument(
        '--minlen', '-min', action='store',  type = int, help='minimum word length')
    arg_parser.add_argument(
        '--maxlen', '-max', action='store',  type = int, help='maximum word length')
    arg_parser.add_argument(
        '--wordfile', '-f', action='store', help='wordfile')

    args = arg_parser.parse_args()

    count = args.count
    minlen = args.minlen
    maxlen = args.maxlen
    wordfile = args.wordfile

    if count is None:
        count = COUNT
    if minlen is None:
        minlen = MINLEN
    if wordfile is None:
        wordfile = WORDFILE

    wordlist = load_words(wordfile, minlen, maxlen)

    total_words = len(wordlist)

    index_array = random_indexes(count, total_words)
    for index in index_array:
        print(wordlist[index])
    print('..out of ' + str(total_words) + ' possible words.')

if __name__ == "__main__":
    main()
