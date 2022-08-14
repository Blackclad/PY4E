fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened',fname)
    exit()

addr = dict()

for line in fhand:
    line = line.rstrip()
    if line.startswith('From '):
        words = line.split()
        address = words[1]
        if address not in addr:
            addr[address] = 1
        else:
            addr[address] += 1

for key in addr:
    print(key, addr[key])