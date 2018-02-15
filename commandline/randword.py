'''Random word tool - display random dictionary words'''
import argparse
import random
import sys

# defaults
COUNT = 3
MINLEN = 3
WORDFILE = 'words.txt'


def load_words(wordfile, minlen, maxlen):
    '''loads a line seperated word file into an array'''
    wordlist = []
    try:
        with open(wordfile) as wf:
            for word in wf:
                wordlen = len(word) - 1  # remove linefeed from word
                if wordlen >= minlen and (maxlen is None or wordlen <= maxlen):
                    wordlist.append(word[:-1])
    except FileNotFoundError:
        sys.exit('Error: cannot open file ' + wordfile)
    return wordlist


def random_indexes(count, num_words):
    '''returns the requested count of random ints between 0 and < num_words'''
    index_array = []
    for _ in range(count):
        index_array.append(random.randint(0, num_words - 1))
    return index_array


def main():
    '''Main routine. Start by parsing args..'''
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument(
        '--count', '-n', action='store', type=int, default=COUNT, help='Number of words')
    arg_parser.add_argument(
        '--minlen', '-min', action='store', type=int, default=MINLEN, help='minimum word length')
    arg_parser.add_argument(
        '--maxlen', '-max', action='store',  type=int, help='maximum word length')
    arg_parser.add_argument(
        '--wordfile', '-f', action='store', default=WORDFILE, help='wordfile')

    args = arg_parser.parse_args()

    # load words from a file into a Python list
    wordlist = load_words(args.wordfile, args.minlen, args.maxlen)
    total_words = len(wordlist)

    # print out random words from the list
    index_array = random_indexes(args.count, total_words)
    for index in index_array:
        print(wordlist[index])
    print('..out of ' + str(total_words) + ' possible words.')


if __name__ == "__main__":
    main()
