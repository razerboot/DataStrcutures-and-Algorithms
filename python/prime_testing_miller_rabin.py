
def pow_mod(a, d, n):
    if d == 1:
        return a % n
    if d % 2 ==0:
        return pow_mod((a * a) % n, d / 2, n)
    else:
        return (a * pow_mod((a * a) % n, (d - 1) / 2, n)) % n


def miller_rabin(n, d, a):
    x = pow_mod(a, d, n)
    if x == 1 or x == n - 1:
        return True

    while d != n - 1:
        x = (x * x) % n
        d *= 2
        if x == 1:
            return False
        if x == n - 1:
            return True

    return False


def extract_odd(n):
    r = 0
    while n % 2 == 0:
        n /= 2
        r += 1
    return n, r


def is_prime(n):
    if n == 1:
        return False
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]
    pn = 9
    for i in xrange(pn):
        if n % primes[i] == 0:
            return n == primes[i]

    d, r = extract_odd(n - 1)
    #print d, r
    for i in xrange(pn):
        if miller_rabin(n, d, primes[i]) is False:
            return False
    return True
