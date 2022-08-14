def chop(t):
    first = t.pop(0)
    last = t.pop(-1)
    return None

def middle(t):
    first = t.pop(0)
    del first
    last = t.pop(-1)
    del last
    middle = t
    print(middle)


mylist = [0,1,2,3,4,5,6]
middle(mylist)