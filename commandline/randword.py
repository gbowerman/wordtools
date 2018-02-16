'''Random word tool - display random dictionary words'''
import argparse
import random
import sys

# defaults
COUNT = 3
MINLEN = 3
WORDFILE = 'words.txt'
PUNC = ',+-#.@#_'


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
        '--password', '-p', action='store_true', default=False, help='generate password')
    arg_parser.add_argument(
        '--wordfile', '-f', action='store', default=WORDFILE, help='wordfile')

    args = arg_parser.parse_args()

    # set a default low value for maxlen if generating a pass phrase and it's not set
    if args.password is True and args.maxlen is None:
        args.maxlen = 5
    
    # load words from a file into a Python list
    wordlist = load_words(args.wordfile, args.minlen, args.maxlen)
    total_words = len(wordlist)
    
    # select random word indexes
    index_array = random_indexes(args.count, total_words)

    # print out random words from the list
    for index in index_array:
        if args.password is True:
            sys.stdout.write(wordlist[index])
            # to do: add random punctuation/uppercase/integer here
            sys.stdout.write(random.choice(PUNC))
        else:
            print(wordlist[index])
    
    if args.password is False:
        print('..out of ' + str(total_words) + ' possible words.')
    else:
        # add a random number to the end of password
        sys.stdout.write(str(random.randint(0,99)))
        print('\n..out of approx ' + str(total_words ** args.count * (len(PUNC) ** args.count) * 100) + ' combinations.')


if __name__ == "__main__":
    main()
