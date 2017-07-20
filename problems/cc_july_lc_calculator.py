from math import ceil, floor
from random import randrange

t = int(raw_input().strip())
#t = 1
for a0 in xrange(1, t + 1):
    n, b = map(int, raw_input().split())
    #n, b = randrange(1, 10 ** 3), randrange(1, 10 ** 3)
    k = n / (2.0 * b)
    #print k
    if k.is_integer():
        ans = (n - k * b) * k
        ans = int(ans)
    else:
        k1 = int(ceil(k))
        k2 = int(floor(k))
        #print k1, k2
        ans = max((n - k1 * b) * k1, (n - k2 * b) * k2)
    print ans