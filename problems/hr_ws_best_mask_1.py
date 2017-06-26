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


print time() - t1