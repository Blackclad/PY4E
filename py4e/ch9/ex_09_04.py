fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened',fname)
    exit()

mbox = dict()

for line in fhand:
    line = line.rstrip()
    if line.startswith('From '):
        words = line.split()
        address = words[1]
        mbox[address] = mbox.get(address,0)+1

bigcount = None
bigaddress = None
for key,value in mbox.items():
    if bigcount is None or value > bigcount:
        bigaddress = key
        bigcount = value
print(bigaddress, bigcount)
