# gen_word_data.sh - use this script to download the word list of your choice
# This example uses Words - the word list behind Letterpress
# Words is licensed under Create Commons - see: https://github.com/atebits/Words/blob/master/LICENSE
# Should the link not work at some point, replace it with another working link to a line separated
# list of words.
curl https://raw.githubusercontent.com/atebits/Words/master/Words/en.txt > en.txt
python3 ./line2csv.py en.txt > en.csv
rm en.txt