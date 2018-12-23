'''Word fine - cheap and cheerful tool to find matching words with wildcards of the form w??d'''
import argparse
import random
import sys
# import time

WORDFILE = 'words.txt'


'''load words of matching length from a file into a list'''
def load_words(wordfile, length):
    '''loads a line seperated word file into an array'''
    wordlist = []
    try:
        with open(wordfile) as wf:
            for word in wf:
                wordlen = len(word) - 1  # remove linefeed from word
                if wordlen == length:
                    wordlist.append(word[:-1])
    except FileNotFoundError:
        sys.exit('Error: cannot open file ' + wordfile)
    return wordlist


'''word_match - return true if partial word matches word'''
def word_match(partial_word, word, wordlen):
    for x in range(wordlen):
        if partial_word[x] == '?':
            continue
        if partial_word[x] != word[x]:
            return False
    return True


def main():
    '''Main routine. Start by parsing args..'''
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument(
        '--word', '-w', action='store', type=str, help='A partial word with ? for missing letters')
    arg_parser.add_argument(
        '--wordfile', '-f', action='store', default=WORDFILE, help='wordfile')

    args = arg_parser.parse_args()

    # load words from a file into a list
    partial_word = args.word
    wordlen = len(partial_word)
    wordlist = load_words(args.wordfile, wordlen)

    # time execution
    # start_time = time.time()

    for word in wordlist:
        if len(word) != wordlen:
            continue
        if word_match(partial_word, word, wordlen):
            print(word)

    # end_time = time.time()
    # print('Execution time: ' + str(end_time - start_time))


if __name__ == "__main__":
    main()
