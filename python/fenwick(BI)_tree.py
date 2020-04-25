#not properly working
from collections import Counter


def seive(n):
    p = []
    vi = [0] * (n + 1)
    i = 2
    while i * i <= n:
        if vi[i] == 0:
            j = i
            while j * i <= n:
                vi[j * i] = 1
                j += 1
        i += 1
    for i in xrange(2, n + 1):
        if vi[i] == 0:
            p.append(i)
    return p

primes = seive(800)
mod = 10 ** 9 + 7


def f(val):
    val = int(val)
    c = Counter()
    old_val = val
    for p in primes:
        if p * p > old_val:
            break
        while val % p == 0:
            val /= p
            c[p] += 1
    if val != 1:
        c[val] += 1

    p1 = old_val
    for key in c:
        p1 = (p1 / key * (key + (key - 1) * c[key])) % mod
    return p1


def modify(ft, i, old_val, val):

    while i <= n:
        ft[i] = (ft[i] - old_val + val) % mod
        i += i & (-1 * i)


def build(ft, arr, n):
    for i in xrange(1, n + 1):
        modify(ft, i, 0, arr[i])


def query(ft, i):
    res = 0
    while i > 0:
        res = (res + ft[i]) % mod
        i -= i & (-1 * i)
    return res


n = input()
arr = [0] + map(f, raw_input().split())
ft = [0] * (n + 1)
build(ft, arr, n)
#print arr, ft
q = input()
for a0 in xrange(q):
    type, x, y = raw_input().split()
    x, y = int(x), int(y)
    if type == 'C':
        print (query(ft, y) - query(ft, x - 1)) % mod
    else:
        old_val = arr[x]
        arr[x] = f(y)
        modify(ft, x, old_val, arr[x])
