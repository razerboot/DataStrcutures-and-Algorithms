from math import log
from time import time

t1 = time()
b = {}
for i in xrange(2, 10 ** 6):
    a = 1
    p = 1
    b[i] = set([])
    while a <= 10 ** 18 and p <= 10 ** 18 / (i * 1.0):
        p *= i
        a += p
        b[i].add(a)


t = input()
for a0 in xrange(t):
    n = input()
    print 'Case #' + str(a0 + 1) + ':',
    for i in xrange(2, 10 ** 6):
        if n in b[i]:
            print i
            break
    else:
        x = ((4 * n - 3) ** 0.5 - 1) / 2
        if x.is_integer():
            print int(x)
        else:
            print n - 1