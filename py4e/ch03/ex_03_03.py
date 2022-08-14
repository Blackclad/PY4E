try:
    scr = input("Enter score: ")
    fscr = float(scr)
except:
    print("Error, please enter a numerical value")
    exit()

if fscr >= 0.0 and fscr <= 1.0:

    if fscr >= .9:
        print("A")
    elif fscr >= .8:
        print("B")
    elif fscr >= .7:
        print("C")
    elif fscr >= .6:
        print("D")
    elif fscr < .6:
        print("F")

else:
    print("Error, out of range")
    exit()