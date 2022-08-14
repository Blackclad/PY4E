import string

fhand = open('words.txt')

letters = dict()
total = 0

for line in fhand:
    line = line.rstrip()
    line = line.lower()
    line = line.translate(line.maketrans('', '', string.punctuation))
    line = line.translate(line.maketrans('', '', string.whitespace))
    line = line.translate(line.maketrans('', '', string.digits))

    for letter in line:
        letters[letter] = letters.get(letter,0)+1
        total += 1

lst = list()
for k,v in list(letters.items()):
    lst.append((v,k))
        
lst.sort(reverse=True)

print('Total letters: ',total)
for v,k in lst:
    print(k,'-',v)