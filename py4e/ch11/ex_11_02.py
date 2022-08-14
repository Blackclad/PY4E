import re

fname = open('regex_sum_1531050.txt')

intlist = []
count = 0

for line in fname:
    line = line.rstrip()    
    num_in_line = re.findall ('[0-9]+', line)
    if len(num_in_line) > 0:
        count = count + 1
        for num in num_in_line:
            num = int(num)
            intlist.append(num)

print('There are',count,'numbers total')
print('The sum of these numbers is',sum(intlist))
