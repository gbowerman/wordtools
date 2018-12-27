'''Word fine - cheap and cheerful tool to find matching words with wildcards of the form w??d'''
import argparse
import sys
# import time

WORDFILE = 'words.txt'


def load_words(wordfile, length):
    '''load words of matching length from a file into a list'''
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


def word_match(partial_word, word, wordlen):
    '''return true if partial word matches word'''
    for x in range(wordlen):
        if partial_word[x] == '?':
            continue
        if partial_word[x] != word[x]:
            return False
    return True


def wordfind(partial_word, wordfile):
    '''finds matching words in a list - '?' is wild'''
    wordlen = len(partial_word)
    wordlist = load_words(wordfile, wordlen)
    for word in wordlist:
        if word_match(partial_word, word, wordlen):
            print(word)


def anagfind(anagram, wordfile):
    '''finds an anagram by comparing two sorted strings'''
    wordlen = len(anagram)
    srtdarr = sorted(anagram)
    wordlist = load_words(wordfile, wordlen)
    for word in wordlist:
        if srtdarr == sorted(word):
            print(word)


def main():
    '''Main routine. Start by parsing args..'''
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument(
        '--word', '-w', action='store', type=str, help='A partial word with ? for missing letters')
    arg_parser.add_argument(
        '--anagram', '-a', action='store', type=str, help='Word to look for anagrams of')
    arg_parser.add_argument(
        '--wordfile', '-f', action='store', default=WORDFILE, help='wordfile')

    args = arg_parser.parse_args()

    # time execution
    # start_time = time.time()

    if args.word is not None:
        wordfind(args.word, args.wordfile)
    if args.anagram is not None:
        anagfind(args.anagram, args.wordfile)

    # end_time = time.time()
    # print('Execution time: ' + str(end_time - start_time))


if __name__ == "__main__":
    main()
