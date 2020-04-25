#!/bin/python

import sys
from time import time
from random import randrange
from fractions import gcd


def check_tuple(tuple, s):
    if s[tuple[1]] != 'b':
        return 0
    if s[tuple[0]] == 'a' and s[tuple[2]] == 'c':
        return 1
    if s[tuple[0]] == 'c' and s[tuple[2]] == 'a':
        return 1
    return 0


def gcd1(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


#n = input()
n = 10 ** 5
arr = ['a', 'b', 'c']
s = ''.join([arr[randrange(0, 3)] for i in xrange(n)])
print s
#s = raw_input()

t1 = time()
i = 1
count = 0
while i * i <= n:
    k = i + 1
    while k * k <= n:
        t = i * i, i * k, k * k
        if gcd(i, k) != 1:
            k += 1
            continue
        x = 1
        while t[0] * x <= n and t[1] * x <= n and t[2] * x <= n:
            if check_tuple((t[0] * x - 1, t[1] * x - 1, t[2] * x - 1), s):
                count += 1
            x += 1
        k += 1
    i += 1
print count
print time() - t1