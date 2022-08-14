def computegrade(score):
    if score >= 0.0 and score <= 1.0:

        if score >= .9:
            grade = "A"
        elif score >= .8:
            grade = "B"
        elif score >= .7:
            grade = "C"
        elif score >= .6:
            grade = "D"
        elif score < .6:
            grade = "F"

    else:
        print("Error, out of range")
        exit()

    return grade

try:
    scr = input("Enter score: ")
    fscr = float(scr)
except:
    print("Error, please enter a numerical value between 0.0 and 1.0")
    exit()

grade = computegrade(fscr)

print("Grade:", grade)