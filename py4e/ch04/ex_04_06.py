def computepay(hours, rate):
    if fh > 40:
        reg = 40 * rate
        ovt = (hours - 40) * (rate * 1.5)
        pay = reg + ovt
        #print(tp)
    else:
        #print(fh * fr)
        pay = hours * rate
    return pay

sh = input("Enter hours: ")
sr = input("Enter rate: ")
fh = float(sh)
fr = float(sr)

xp = computepay(fh,fr)

print("Pay:", xp)



