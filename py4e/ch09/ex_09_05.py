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
        delimiter = '@'
        address = address.split(delimiter)
        domain = address[1]             
        mbox[domain] = mbox.get(domain,0)+1
       
for key in mbox:
    print(key, mbox[key])









 # if address.startswith('@ ') not in mbox:
        #     mbox[address] = 1
        # else:
        #     mbox[address] += 1