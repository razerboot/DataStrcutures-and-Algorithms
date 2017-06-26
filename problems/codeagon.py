# Enter your code here. Read input from STDIN. Print output to STDOUT
import math


def find_mod(b, m):
    inv = pow1(b, m - 2, m) % m
    return inv


def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


def pow1(a, b, m):
    if b == 0:
        return 1
    if b % 2 == 0:
        return pow1((a * a) % m, b / 2, m)
    else:
        return (a * pow1((a * a) % m, (b - 1) / 2, m)) % m


m = (10 ** 9) + 7

T_arr = {}


def T(T_arr, n, d):
    if n < 0:
        return
    h = str(n) + "#" + str(d)
    if h in T_arr:
        return T_arr[h]
    if n == 0:
        # value = 1*find_mod(d,m)
        value = 1, d
    else:
        # value = ((n+1)*find_mod((T(T_arr,n-1,d)+1),m)%m)%m
        buff = T(T_arr, n - 1, d)
        val1 = ((n + 1) * buff[1]) % m
        val2 = (buff[0] + buff[1]) % m
        gcd1 = gcd(val1, val2)
        val1 /= gcd1
        val2 /= gcd1
        value = val1, val2
    T_arr[h] = value
    return value


def func1(T_arr, arr, m):
    if arr[1] < 0 or arr[2] < 0 or arr[3] < 0:
        return
    i = arr[1]
    num = 1
    den = 1
    while (i <= arr[2]):
        val = T(T_arr, i, arr[3])
        num = (num * val[0]) % m
        den = (den * val[1]) % m
        i += 1
    # gcd1 = gcd(num,den)
    # num /= gcd1
    # den /= gcd1
    # print num
    # print den
    if num % den == 0:
        return num / den
    else:
        return (num * find_mod(den, m)) % m


def func2(T_arr, arr1, m):
    n = arr1[1]
    m1 = arr1[2]
    d = arr1[3]
    if n < 0 or m1 < 0 or d < 0:
        return
    k = 0
    num = 1
    den = 1
    while (k <= m1):
        val = T(T_arr, n, d + k)
        num = (num * val[0]) % m
        den = (den * val[1]) % m
        k += 1
    # gcd1 = gcd(num,den)
    # num /= gcd1
    # den /= gcd1
    if num % den == 0:
        return num / den
    else:
        return (num * find_mod(den, m)) % m




q = int(raw_input())
q1 = math.floor(3.0 * q / 4.0)
q2 = q - q1

i = 1
while (i <= q1):
    arr = map(int, raw_input().strip().split(' '))
    print func1(T_arr, arr, m)
    i += 1
i = 1
while (i <= q2):
    arr = map(int, raw_input().strip().split(' '))
    # print arr
    print func2(T_arr, arr, m)
    i += 1
# print T_arr


