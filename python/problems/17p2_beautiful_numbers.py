from math import log
t =input()
for a0 in xrange(t):
    n = input()
    print 'Case #' + str(a0 + 1) +':',
    for i in xrange(2, n):
        if log((i - 1) * n + 1, i).is_integer():
            print i
            break