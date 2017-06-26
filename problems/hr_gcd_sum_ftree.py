#http://www.geeksforgeeks.org/eulers-totient-function-for-all-numbers-smaller-than-or-equal-to-n/
from collections import defaultdict, Counter
from time import time

MOD = 10 ** 9 + 7


def mod(num):
    return (num % MOD + MOD) % MOD


def cal_phi(n):
    #using technique of seive and euler's totent function in the from of prime product formula
    phi = [i for i in xrange(n + 1)]
    for i in xrange(2, n + 1):
        if phi[i] == i:
            for j in xrange(i, n + 1, i):
                phi[j] -= phi[j] / i
                phi[j] = mod(phi[j])
    return phi


def cal_pillai(n):
    phi = cal_phi(n)
    p = [0] * (n + 1)
    for i in xrange(1, n + 1):
        for j in xrange(i, n + 1, i):
            p[j] += i * phi[j / i]
    return p


def modify(st, i, val, n):
    i += n
    st[i] = val
    while i > 1:
        st[i / 2] = (st[i] + st[i ^ 1]) % MOD
        i /= 2


def build(st, n):
    for i in reversed(xrange(1, n)):
        st[i] = (st[2 * i] + st[2 * i + 1]) % MOD


def query(st, l, r, n):
    res = 0
    l, r = l + n, r + n
    while l < r:
        if l % 2 != 0:
            res = (res + st[l]) % MOD
            l += 1
        if r % 2 != 0:
            r -= 1
            res = (res + st[r]) % MOD
        l, r = l / 2, r / 2
    return res

t1 = time()
p = cal_pillai(5 * 10 ** 5)
#print p
#print time() - t1
n = input()
arr = map(int, raw_input().split())
st = [0] * (2 * n)
for i in xrange(n):
    st[i + n] = p[arr[i]]
build(st, n)
q = input()
for a0 in xrange(q):
    type, x, y = raw_input().split()
    x, y = int(x), int(y)
    if type == 'C':
        print query(st, x - 1, y, n)
    else:
        modify(st, x - 1, p[y], n)
