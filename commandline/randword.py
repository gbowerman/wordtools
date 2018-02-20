'''Random word tool - display random dictionary words, generate password'''
import argparse
import random
import sys
# import time

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


def random_words(count, wordlist):
    '''return the requested number of random words from a word list'''
    rand_words = []
    for _ in range(count):
        rand_words.append(random.choice(wordlist))
    return rand_words


def gen_passphrase(word_array):
    '''generate a password from a word list, adding random punctuation and numerals'''
    passphrase = ''
    for word in word_array:
        # randomly capitalize
        if bool(random.getrandbits(1)):
            word = word.capitalize()
        # randomly replace letter with number
        if bool(random.getrandbits(1)):
            if 'o' in word:
                word = word.replace('o', '0')
            elif 'i' in word:
                word = word.replace('i', '1')
            elif 'e' in word:
                word = word.replace('e', '3')
            elif 's' in word:
                word = word.replace('s', '5')
        passphrase += word + random.choice(PUNC)
    # add a random number to the end of password
    passphrase += str(random.randint(0, 99))
    return passphrase


def main():
    '''Main routine. Start by parsing args..'''
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument(
        '--count', '-n', action='store', type=int, default=COUNT, help='Number of random words')
    arg_parser.add_argument(
        '--repeat', '-r', action='store', type=int, default=1, help='Number of pass phrases to gnerate')
    arg_parser.add_argument(
        '--minlen', '-min', action='store', type=int, default=MINLEN, help='minimum word length')
    arg_parser.add_argument(
        '--maxlen', '-max', action='store',  type=int, help='maximum word length')
    arg_parser.add_argument(
        '--password', '-p', action='store_true', default=False, help='generate password')
    arg_parser.add_argument(
        '--wordfile', '-f', action='store', default=WORDFILE, help='wordfile')

    args = arg_parser.parse_args()

    # set default low val for maxlen if generating passphrase and not set
    if args.password is True and args.maxlen is None:
        args.maxlen = 5

    # load words from a file into a list
    wordlist = load_words(args.wordfile, args.minlen, args.maxlen)
    total_words = len(wordlist)

    # time execution
    # start_time = time.time()

    if args.password is True: # generate pass phrase
        for _ in range(args.repeat):
            word_array = random_words(args.count, wordlist)
            print(gen_passphrase(word_array))
        # entropy depends on word range & number, punctuation, capitalization, numeric etc.
        # remember to update entropy calculation if modifying gen_passphrase()
        entropy = total_words ** args.count * (len(PUNC) ** args.count) * (2 ** args.count) * (2 ** args.count) * 100
        print('\n..out of approx ' + '{:,}'.format(entropy) + ' combinations.')
    else:
        # list of words
        word_array = random_words(args.count, wordlist)
        print('\n'.join(word_array))
        print('..out of ' + str(total_words) + ' possible words.')

    # end_time = time.time()
    # print('Execution time: ' + str(end_time - start_time))


if __name__ == "__main__":
    main()
