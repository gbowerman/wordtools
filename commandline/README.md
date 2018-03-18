
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
c:\>python randword.py -p
tyin#gle1s@77
..out of approx 38,905,657,753,600 combinations.

# generate a passphrase based on 3 words no longer than 4 letters each:
c:\>python randword.py -p -n 3 -max 4
du3d-brit+Sus.19
..out of approx 1,048,160,395,981,619,200 combinations.

# generate 5 passphrases, each based on 2 random words:
c:\>python randword.py -r 5 -p
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


## Renamer
File renaming tool - not a 'wordtool' but leaving it here until I create a file tools repo

### Usage

```
usage: renamer.py [-h] --ext EXT [--remove REMOVE] [--trunc TRUNC] [--pre PRE]
                  [--append APPEND]
renamer.py: error: the following arguments are required: --ext/-e
```
### Examples
```
# remove the string 'test' from every MP3 file in the current folder
python .\renamer.py --remove test --ext mp3
Renaming "nametest1.mp3" to "name1.mp3".
Renaming "nametest2.mp3" to "name2.mp3".
Renaming "nametest3.mp3" to "name3.mp3".
Renaming "nametest4.mp3" to "name4.mp3".
Renaming "nametest5.mp3" to "name5.mp3".
5 files renamed.

# Add the string 'thisis' to the beginning, and truncate 'file' from the end of all MP3 files in the current folder..
python .\renamer.py --ext mp3 --pre thisis --trunc file
Renaming "mytest1file.mp3" to "thisismytest1.mp3".
Renaming "mytest2file.mp3" to "thisismytest2.mp3".
Renaming "mytest3file.mp3" to "thisismytest3.mp3".
Renaming "mytest4file.mp3" to "thisismytest4.mp3".
Renaming "mytest5file.mp3" to "thisismytest5.mp3".
5 files renamed.

# append the string 'file' to the end of all MP3 files in the current folder..
python .\renamer.py --ext mp3 --append file
Renaming "thisismytest1.mp3" to "thisismytest1file.mp3".
Renaming "thisismytest2.mp3" to "thisismytest2file.mp3".
Renaming "thisismytest3.mp3" to "thisismytest3file.mp3".
Renaming "thisismytest4.mp3" to "thisismytest4file.mp3".
Renaming "thisismytest5.mp3" to "thisismytest5file.mp3".
5 files renamed.

# truncate all MP3 files in current folder from last 'f'
python .\renamer.py --ext mp3 --trunc f
Renaming "thisismytest1file.mp3" to "thisismytest1.mp3".
Renaming "thisismytest2file.mp3" to "thisismytest2.mp3".
Renaming "thisismytest3file.mp3" to "thisismytest3.mp3".
Renaming "thisismytest4file.mp3" to "thisismytest4.mp3".
Renaming "thisismytest5file.mp3" to "thisismytest5.mp3".
5 files renamed.
```
