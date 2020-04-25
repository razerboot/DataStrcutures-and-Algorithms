from fractions import gcd, Fraction
from math import floor

d = [0]


def gcd_extended(a, b, x, y):
    if b == 0:
        d[0] = a
        x[0] = 1
        y[0] = 0
    else:
        gcd_extended(b, a % b, x, y)
        temp = x[0]
        x[0] = y[0]
        y[0] = temp - (a / b) * y[0]


t = input()
mod1, mod2 = 10 ** 9 + 7, 10 ** 9 + 9
for a0 in xrange(1, t + 1):
    n = input()
    if n == 1:
        p, q = 0, 0
    else:
        g = gcd(n * (n - 1), 2 * (2 * n - 3))
        p = n * (n - 1) / g
        q = 2 * (2 * n - 3) / g
    x, y = [0], [0]
    gcd_extended(q, mod1, x, y)
    inv1 = (x[0] + mod1) % mod1
    x, y = [0], [0]
    gcd_extended(q, mod2, x, y)
    inv2 = (x[0] + mod2) % mod2

    ans1 = ((p % mod1) * inv1) % mod1
    ans2 = ((p % mod2) * inv2) % mod2

    print ans1, ans2
