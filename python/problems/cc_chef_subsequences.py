from random import randrange
from time import time
from math import log
from itertools import combinations


def backtrack(arr, n, k, sol):
    for i in xrange(1, n + 1):
        for comb in combinations(xrange(n), i):
            sum = 0
            for j in comb:
                sum += arr[j]
            if sum <= k:
                sol.append(sum)


def bs(arr, val, n):
    l = 0
    r = n
    while r - l > 1:
        mid = (l + r) / 2
        if arr[mid] <= val:
            l = mid
        else:
            r = mid
    return l + 1


def f(a):
    return log(int(a), 2)

t1 = time()
n, k = map(int, raw_input().split())
arr = map(f, raw_input().split())
#n = 30
#k = f(randrange(10 ** 16, 10 ** 18))
#arr = [f(randrange(10 ** 1, 10 ** 3)) for i in xrange(n)]
#print k
#print arr
k = f(k)
mid = n / 2
arr1 = arr[:mid]
arr2 = arr[mid:]
sol1 = []
sol2 = []
buff = [0]
#print arr1, arr2
backtrack(arr1, len(arr1), k, sol1)
backtrack(arr2, len(arr2), k, sol2)
#print sol1, sol2
sol2.sort()
m = len(sol2)
c = 0
for ele in sol1:
    val = k - ele
    if val == sol2[0]:
        c += 1
    elif val > sol2[0]:
        c += bs(sol2, val, m)
print c + len(sol1) + len(sol2)
#print time() - t1

