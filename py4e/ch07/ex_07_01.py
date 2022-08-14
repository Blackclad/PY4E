from operator import contains


fhand = open('mbox-short.txt') 

for line in fhand:
    lines = line.rstrip()
    print(lines)