
# Command line word tools

Command line based word Python finding tools.

## randword.py

Returns the requested number of random words, optionally specifying min and max word lengths.

```
usage: randword.py [-h] [--count COUNT] [--minlen MINLEN] [--maxlen MAXLEN]
                   [--wordfile WORDFILE]

optional arguments:
  -h, --help            show this help message and exit
  --count COUNT, -n COUNT
                        Number of words - default 3
  --minlen MINLEN, -min MINLEN
                        minimum word length - default 3
  --maxlen MAXLEN, -max MAXLEN
                        maximum word length - default None
  --wordfile WORDFILE, -f WORDFILE
                        wordfile - default words.txt

Examples:

# return 3 random words of minimum length 3:
c:\>python randword.py

conductibility
ingrainedness
caninities
..out of 274802 possible words.

# return 5 random words of minimum length 6, maximum length 7:
c:\>python randword.py -n 5 -min 6 -max 7

behoove
viners
fauchon
bagwash
ouriest
..out of 55713 possible words.

```

### Installation
Expects a line separated word file called 'words.txt' in the current directory.

On Windows versions which support _curl_ you can use the _get_words.bat_ file to download one.
 