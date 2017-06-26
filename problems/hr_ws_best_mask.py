from itertools import combinations
from time import time
from random import randrange


def add_to_set(ele, sets, powers, h):

    for i in xrange(h):
        if powers[i] & ele != 0:
            if sets[i] is None:
                sets[i] = {ele}
            else:
                sets[i].add(ele)


def find_highest_bit(arr, powers):
    high = 0
    for ele in arr:
        for i in reversed(xrange(26)):
            if powers[i] & ele != 0:
                if i > high:
                    high = i
                break
    return high


def check_comb(sets, h, i, n, unions):

    for comb in combinations(range(h), i):
        u = set([])
        if len(comb) == 1:
            if sets[comb[0]] is not None:
                u |= sets[comb[0]]
                unions[comb] = u
        else:
            r = comb[-1]
            l = comb[:-1]
            u = unions[l] | unions[(r,)]
            unions[comb] = u

        if len(u) == n:
            return 1, comb
    return 0, comb


def check_all_comb_binary(sets, h, n, unions):
    l = 1
    r = h
    while r - l > 1:
        mid = (l + r) / 2
        flag, val = check_comb(sets, h, mid, n, unions)
        if flag:
            r = mid
        else:
            l = mid
    flag, val = check_comb(sets, h, r, n, unions)
    return val


def check_all_comb(sets, h, n, unions):
    for i in xrange(1, h + 1):
        flag, val = check_comb(sets, h, i, n, unions)
        if flag:
            return val

#n = input()
n = 10 ** 5

powers = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288,
          1048576, 2097152, 4194304, 8388608, 16777216, 33554432]
#arr = set(map(int, raw_input().split()))
arr = set([randrange(1, 2 ** 13) for i in xrange(n)])
n = len(arr)

t1 = time()
h = find_highest_bit(arr, powers) + 1

sets = [None] * h

for ele in arr:
    add_to_set(ele, sets, powers, h)

unions = {}
comb = check_all_comb(sets, h, n, unions)

num = 0
for i in comb:
    num += powers[i]
print num
print time() - t1