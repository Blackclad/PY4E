fname = input('Enter file name: ')
try:
    fhand = open(fname)
except:
    print('Invalid file name')
    exit()

mbox = dict()

for line in fhand:
    line = line.rstrip()
    if line.startswith('From '):
        portion = line.split()
        time = portion[5].split(':')
        hour = time[0]
        mbox[hour] = mbox.get(hour,0)+1

lst = list()
for k,v in list(mbox.items()):
    lst.append((k,v))

lst.sort()

for k,v in lst:
    print(k,v)