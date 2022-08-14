import re

fname = input('Emter file name: ')
try:
    fhand = open(fname)
except:
    print('Invalid file name')

grep = input('Enter a regular expression: ')
count = 0
for line in fhand:
    if re.search(grep, line):
        count += 1

print(fname,'had',count,'lines that matched',grep)