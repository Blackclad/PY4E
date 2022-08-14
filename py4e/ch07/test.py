import datetime
now = datetime.datetime.now()
print(now)

fhand = open('mbox-short.txt')

newlist = list()
for line in fhand:
    line = line.rstrip()
    if line.startswith('X-DSPAM-Confidence:'):
        data = line.lstrip('X-DSPAM-Confidence: ')
        break
data = float(data)
data = list(data)
print(sum(data))
        # numbers = data.split()
        