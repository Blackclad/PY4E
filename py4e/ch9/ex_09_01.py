fhand = open('words.txt')

dword = dict()

for lines in fhand:
    line = lines.split() #Breaking lines into lists of words.
    for words in line: #Looping through each word in the line.
        dword[words] = 'value'

while True:
    cword = input('Enter a word: ')
    if cword == 'done':
        print('Exiting'), exit()
    elif cword in dword:
        print('This word is included')
        continue
    elif print('This word is not included'):
        continue