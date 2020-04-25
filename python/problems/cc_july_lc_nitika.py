t = input()
for a0 in xrange(1, t + 1):
    s = raw_input().split()
    if len(s) == 1:
        print s[0].title()
    else:
        for i in xrange(len(s) - 1):
            print s[i][0].upper() + '.',
        print s[-1].title()

