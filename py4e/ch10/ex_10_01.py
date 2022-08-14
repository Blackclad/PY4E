fname = input('Enter file name: ')
try:
    fhand = open(fname)
except:
    print('Invalid file')
    exit()

mbox = dict()

for line in fhand:
    line = line.rstrip()
    if line.startswith('From '):
        words = line.split()
        address = words[1]
        mbox[address] = mbox.get(address,0)+1

lst = list()
for k,v in list(mbox.items()):
    lst.append((v,k))

lst.sort(reverse=True)

for k,v in lst:
    print(k,v)

print(' ')

bigcount = None
bigaddress = None
for k,v in mbox.items():
    if bigcount is None or v > bigcount:
        bigaddress = k
        bigcount = v
print(bigcount, bigaddress)



# for k,v in mbox.items():
#     print(k,v)