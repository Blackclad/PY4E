fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened',fname)
    exit()

days = dict()

for line in fhand:
    line = line.rstrip()
    if line.startswith('From '):
        words = line.split()
        day = words[2]
        if day not in days:
            days[day] = 1
        else:
            days[day] += 1

for key in days:
    print(key, 'occured', days[key], 'times')