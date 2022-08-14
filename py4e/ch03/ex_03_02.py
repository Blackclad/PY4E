
try:
    sh = input("Enter hours: ")
    fh = float(sh)
except:
    print("Error, please enter a numeric input")
    exit()
try:
    sr = input("Enter rate: ")
    fr = float(sr)
except:
    print("Error, please enter a numeric input")
    exit()
if fh > 40:
    reg = 40 * fr
    ovt = (fh - 40) * (fr * 1.5)
    tp = reg + ovt
    print(tp)
else:
    print(fh * fr)