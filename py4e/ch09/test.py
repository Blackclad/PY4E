import string                                                           #line.translate(str.maketrans(fromstr, tostr, deletestr)

fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

counts = dict()
for line in fhand:
    line = line.rstrip()                                                #Strip away unwanted whitespace.
    line = line.translate(line.maketrans('', '', string.punctuation))   #Use the translate method to "delete" all punctuation.
    line = line.lower()                                                 #Make all lines lower case
    words = line.split()                                                    #Breaking each line into a list of words.
    for word in words:
        counts[word] = counts.get(word,0)+1                                                #Looping through each word in the line.
        # if word not in counts:
        #     counts[word] = 1
        # else:
        #     counts[word] += 1

for key in counts:
    print(key, counts[key])