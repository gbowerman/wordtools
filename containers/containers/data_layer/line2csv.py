# simple python3 script to convert a list of words (one on each line) to a CSV file consisting of
# word and word length, suitable for loading into a database
tf = 'en.txt'
f = open(tf)
for line in f:
    line = line.rstrip()
    if line.count("'") == 0 and line.count(" ") == 0:
        print("0," + line + "," + str(len(line)))
f.close()