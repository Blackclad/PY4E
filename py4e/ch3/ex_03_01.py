sh = input("Enter hours: ")
sr = input("Enter rate: ")
fh = float(sh)
fr = float(sr)

if fh > 40:
    reg = 40 * fr
    ovt = (fh - 40) * (fr * 1.5)
    tp = reg + ovt
    print(tp)
else:
    print(fh * fr)