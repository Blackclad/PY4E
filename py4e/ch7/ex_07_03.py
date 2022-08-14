fhand = input('Enter file name: ')
if fhand == 'na na boo boo':
    print("NA NA BOO BOO TO YOU - You have been punk'd!")
    exit()
else:
    try:
        fhand = open(fhand)
    except:
        print('Enter a valid file name')
        exit()

total = 0
count = 0
for line in fhand:
    line = line.rstrip()
    if line.startswith('X-DSPAM-Confidence:'):
        data = line.lstrip('X-DSPAM-Confidence: ')
        data = float(data)
        total = total + data
        count = count + 1

print('Average spam confidence:',total / count)