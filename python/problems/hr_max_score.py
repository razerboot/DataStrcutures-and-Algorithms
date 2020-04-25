from time import time
from random import randrange
from math import log


def get_max_score(a, n):
    m = 1 << n
    v = [0] * m
    ss = [0] * m
    for l in range(n):
        ml = 1 << l
        for i in range(ml, ml + ml):
            it = i ^ ml
            s = a[l] + ss[it]
            ss[i] = s
            rb = v[it] + s % a[l]

            while it > 0:
                itn = it & (it - 1)
                b = it ^ itn
                r = v[i ^ b] + s % ss[b]
                if (r > rb): rb = r;
                it = itn
            v[i] = rb

    print v[m - 1]


def max_total_score(arr, n):
    m = 1 << n
    sum_array = [0] * m
    dp = [0] * m
    powers = [1] * n
    for i in xrange(1, n):
        powers[i] = powers[i - 1] * 2
    for i in xrange(n):
        sum_array[powers[i]] = arr[i]

    for mask in xrange(1, m):
        mask2 = mask
        i = mask2 & -1 * mask2
        mask3 = mask2 & mask2 - 1
        sum_array[mask] = sum_array[mask3] + sum_array[i]

        while mask2 > 0:
            i = mask2 & -1 * mask2
            mask2 &= mask2 - 1
            mask1 = mask ^ i
            temp = dp[mask1] + sum_array[mask1] % sum_array[i]
            if dp[mask] < temp: dp[mask] = temp

    print dp[m - 1]



#n = input()
#arr = map(int, raw_input().split())
n = 20
arr = [randrange(1, 10 ** 16) for i in xrange(n)]
t1 = time()
max_total_score(arr, n)
t2 = time()
print t2 - t1
get_max_score(arr, n)
print time() - t2