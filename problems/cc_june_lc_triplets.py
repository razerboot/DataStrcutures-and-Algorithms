from time import time
from random import randrange


def find_floor(arr, val, i, n):
    l = i
    r = n
    if val < arr[i]:
        return -1

    while r - l > 1:
        mid = (l + r) / 2

        if arr[mid] > val:
            r = mid
        else:
            l = mid
    return l

t1 = time()
mod = 1000000007
#t = input()
t = 10
tt = 0
tt1 = 0
tt2 = 0
for a0 in xrange(t):
    f = int
    p, q, r = 10 ** 5, 10 ** 5, 10 ** 5

    t2 = time()
    a = [randrange(10 ** 3, 1000000001) for i in xrange(p)]
    b = [randrange(10 ** 3, 1000000001) for i in xrange(q)]
    c = [randrange(10 ** 3, 1000000001) for i in xrange(r)]
    tt += time() - t2
    # p, q, r = map(f, raw_input().split())
    #a = map(f, raw_input().split())
    #b = map(f, raw_input().split())
    #c = map(f, raw_input().split())
    t4 = time()

    a.sort()
    b.sort()
    c.sort()

    a_prefix = [0] * p
    c_prefix = [0] * r

    for i in xrange(p):
        if i == 0:
            a_prefix[i] = a[i]
        else:
            a_prefix[i] = (a_prefix[i - 1] + a[i]) % mod

    for i in xrange(r):
        if i == 0:
            c_prefix[i] = c[i]
        else:
            c_prefix[i] = (c_prefix[i - 1] + c[i]) % mod

    yc = find_floor(b, c[0], 0, q)
    ya = find_floor(b, a[0], 0, q)
    if ya == -1 and yc == -1:
        yb = 0
    else:
        yb = max(ya, yc)

    tt2 += time() - t4

    ans = 0
    prev_x = 0
    prev_z = 0
    for i in xrange(yb, q):
        t3 = time()
        x = find_floor(a, b[i], prev_x, p)
        tt1 += time() - t3
        if x == -1:
            continue
        t3 = time()
        z = find_floor(c, b[i], prev_z, r)
        tt1 += time() - t3
        if z == -1:
            continue
        nx = x + 1
        nz = z + 1
        prev_x = x
        prev_z = z
        ans = (ans + (((nx * b[i]) % mod + a_prefix[x]) % mod * ((nz * b[i]) % mod + c_prefix[z]) % mod) % mod) % mod


    print ans
print time() - t1
print tt
print tt1
print tt2