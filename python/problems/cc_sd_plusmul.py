from random import randrange
from time import time
t = input()
#t1 = time()
#t = 1
mod = 10 ** 9 + 7
for a0 in xrange(t):
    n = input()
    a = map(int, raw_input().split())
    #n = randrange(10 ** 5, 10 ** 6)
    #a = [randrange(10 ** 8, 10 ** 9) for i in xrange(n)]
    powers = [0] * n
    powers[0] = 1

    s_prefix = [0] * n
    s_prefix[0] = a[0]

    prod_prefix = [0] * n
    prod_prefix[0] = a[0]

    last = 0
    for i in xrange(1, n):
        prod_prefix[i] = (a[i] * ((powers[i - 1] + prod_prefix[i - 1]) % mod)) % mod

        powers[i] = (powers[i - 1] * 2) % mod

        s_prefix[i] = (s_prefix[i - 1] + prod_prefix[i]) % mod

        if i == n - 1:
            last = s_prefix[i]

        s_prefix[i] = (s_prefix[i] + s_prefix[i - 1]) % mod

    if n == 1:
        print a[0]
    else:
        print last

#print time() - t1