#this code works for modfications on range of array like addition or subtraction
# and query for single element or complete array after a set of modifications
from operator import itemgetter as it


def modify(st, l, r, val, n):
    l, r = l + n, r + n
    while l <= r:
        if l % 2 != 0:
            st[l] += val
            l += 1
        if r % 2 == 0:
            st[r] += val
            r -= 1
        if l == r:
            break
        l, r = l / 2, r / 2


def query(st, p, n):
    p += n
    res = 0
    while p > 0:
        res += st[p]
        p /= 2
    return res


def bs(st, x, n):
    l, r = -1, n
    while r - l > 1:
        mid = (l + r) / 2
        val = query(st, mid, n)
        if val <= x:
            l = mid
        else:
            r = mid
    l += 1
    return l


def push(st, n):
    for i in xrange(1, n):
        st[2 * i] += st[i]
        st[2 * i + 1] += st[i]
        st[i] = 0


def f(x, y):
    return int(x), y

n = input()
arr = map(f, raw_input().split(), [i for i in xrange(n)])
arr.sort(key=it(0))
st = [0] * (2 * n)
for i in xrange(n):
    st[i + n] = arr[i][0]

m = input()
for a0 in xrange(m):
    val = input()
    index = bs(st, val, n)
    if index != n:
        modify(st, index, n - 1, -1, n)

push(st, n)

out = [0] * n
for i in xrange(n):
    out[arr[i][1]] = str(st[i + n])
print ' '.join(out)