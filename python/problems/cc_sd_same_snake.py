
def check(x1, x2, x3, x4):
    if x1 > x2:
        x1, x2 = x2, x1
    if x3 > x4:
        x3, x4 = x4, x3

    if x3 > x2:
        return 'no'
    if x4 < x1:
        return 'no'
    return 'yes'


t = input()
for _ in xrange(t):
    x11, y11, x12, y12 = map(int, raw_input().strip().split())
    x21, y21, x22, y22 = map(int, raw_input().strip().split())
    #d for direction if d is 0 snake in row else column
    d1 = 0
    if x11 == x12:
        d1 = 1
        if y11 == y12:
            d1 = 2
    d2 = 0
    if x21 == x22:
        d2 = 1
        if y21 == y22:
            d2 = 2
    if d1 == d2:
        if d1 == 0 and y11 == y21:
            print check(x11, x12, x21, x22)
        elif d1 == 1 and x11 == x21:
            print check(y11, y12, y21, y22)
        elif d1 == 2:
            if (x11, y11) == (x21, y21):
                print 'yes'
            else:
                print 'no'
        else:
            print 'no'
    elif d1 == 2 or d2 == 2:
        if (d1 == 0 or d2 == 0) and y11 == y21:
            print check(x11, x12, x21, x22)
        elif (d1 == 1 or d2 == 1) and x11 == x21:
            print check(y11, y12, y21, y22)
        else:
            print 'no'
    else:
        if (x11, y11) == (x21, y21) or (x11, y11) == (x22, y22) or (x12, y12) == (x21, y21) or (x12, y12) == (x22, y22):
            print 'yes'
        else:
            print 'no'
