word = input('Enter a word: ')
letter = input('Enter a letter: ')

def count(word,letter):
    count=0
    for char in word:
        if letter is char:
            count = count + 1
    print(count)

count(word,letter)