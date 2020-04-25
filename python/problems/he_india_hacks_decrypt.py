from collections import defaultdict, Counter
from time import time
from random import randrange


def find_factors(n, primes):
    factors = defaultdict(list)
    for p in primes:
        for i in xrange(p, n + 1, p):
            factors[i].append(p)
    return factors


def factorize(num, p):
    old_num = num
    for prime in p:
        while num % prime == 0:
            num /= prime
    if num != 1:
        p.append(num)
    return p


def can_decrypt(arr1, num, p, m):
    if m == 2 and p[0] * p[1] == num:
        return 'YES'
    if m == 1:
        if p[0] * p[0] == num:
            return 'YES'
        elif p[0] == num:
            return 'NO'
    for i in xrange(m):
        for j in xrange(i, m):
            if i == j and num % (p[i] * p[i]) != 0:
                continue
            if num / (p[i] * p[j]) in arr1:
                #print num, p[i], p[j]
                return 'YES'
    return 'NO'


#n, q = map(int, raw_input().split())
#arr = map(int, raw_input().split())
n, q = 10 ** 5, 10 ** 6
arr = [randrange(1, 10 ** 6 + 1) for i in xrange(n)]
arr1 = set()
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107,
          109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229,
          233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359,
          367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491,
          499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641,
          643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787,
          797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941,
          947, 953, 967, 971, 977, 983, 991, 997]
t1 = time()
factors = find_factors(10 ** 6, primes)
t = time() - t1
#print factors
for i in xrange(n):
    ele = arr[i]
    if ele > 1:
        while ele <= 10 ** 6:
            arr1.add(ele)
            ele *= arr[i]
#print arr1
t2, t3 = 0, 0
fact = {}
num = 0
t4 = time()
for a0 in xrange(q):
    #num = input()
    #num = randrange(2, 10 ** 6 + 1)
    num += 1
    if num <= 1:
        print 'NO'
    elif num in fact:
        print fact[num]
    else:
        t1 = time()
        if num > 10 ** 3:
            p = factorize(num, factors[num])
        else:
            p = factors[num]
        t2 += time() - t1
        m = len(p)
        t1 = time()
        fact[num] = can_decrypt(arr1, num, p, m)
        #print fact[num]
        t3 += time() - t1
print time() - t4
print t, t2, t3, t + t2 + t3