fname = input("Enter file name: ")
fhand = open(fname)

unique = list()
for line in fhand:
    words = line.split()
    for word in words:
       if word not in unique:
           unique.append(word)
unique.sort()
print(unique)