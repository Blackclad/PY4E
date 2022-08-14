fname = input("Enter file name: ")
fhand = open(fname)

count = 0
for line in fhand:
    lines = line.rstrip()
    if lines.startswith('From '):
        count = count + 1
        lines = lines.split()
        print(lines[1])
        
print("There were", count, "lines in the file with From as the first word")
