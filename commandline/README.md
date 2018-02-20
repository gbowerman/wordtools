
# Command line word tools

Command line based word Python finding tools.

## randword.py

Returns the requested number of random words, optionally specifying min and max word lengths.

```
usage: randword.py [-h] [--count COUNT] [--repeat REPEAT] [--minlen MINLEN]
                   [--maxlen MAXLEN] [--password] [--wordfile WORDFILE]

optional arguments:
  -h, --help            show this help message and exit
  --count COUNT, -n COUNT
                        Number of random words
  --repeat REPEAT, -r REPEAT
                        Number of pass phrases to gnerate
  --minlen MINLEN, -min MINLEN
                        minimum word length
  --maxlen MAXLEN, -max MAXLEN
                        maximum word length
  --password, -p        generate password
  --wordfile WORDFILE, -f WORDFILE
                        wordfile

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

# generate a passphrase based on 3 random words:
c:\>python randword.py -p
Neat,lank_Banco#64
..out of approx 24,267,170,589,861,478,400 combinations.

# generate a passphrase based on 2 words:
c:\>python randword.py -p -n 2
tyin#gle1s@77
..out of approx 38,905,657,753,600 combinations.

# generate a passphrase based on 3 words no longer than 4 letters each:
c:\>python randword.py -p -max 4
du3d-brit+Sus.19
..out of approx 1,048,160,395,981,619,200 combinations.

# generate 5 passphrases, each based on 2 random words:
c:\>python randword.py -r 5 -p -n 2
chips@b0ll#94
Hobs+areas@83
Conns@Y3lms.43
Bines+Cedes,35
gans_p1nes+39

..out of approx 38,905,657,753,600 combinations.
```

### Installation
Expects a line separated word file called 'words.txt' in the current directory.

The word file used in the examples above was downloaded with thanks from the excellent [atebits/Words](https://github.com/atebits/Words) repo.

Use the _get_words.bat_ script to download it. This script uses curl. Make sure curl is in your path. Convert the script from .bat to .sh to run on Linux.
 