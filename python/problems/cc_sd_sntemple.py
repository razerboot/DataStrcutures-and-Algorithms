from random import randrange
from time import time


def linear_check(arr, seq, l, n):
    #print arr, seq
    costs = [0] * n

    max_diff = 0

    for i in xrange(l):
        if arr[i] < seq[i]:
            diff = seq[i] - arr[i]
            if max_diff == -1 or max_diff < diff:
                max_diff = diff

    if max_diff == 0:
        costs[l - 1] = 1

    for i in xrange(1, n - l + 1):
        if max_diff > 0:
            max_diff -= 1

        r = i + l - 1
        if arr[r] < seq[-1]:
            diff = seq[-1] - arr[r]
            max_diff = max(max_diff, diff)

        elif max_diff == 0:
            costs[r] = 1

    #print costs
    return costs


def is_possbile(arr, range, n, arr_sum):

    if range == 1:
        for ele in arr:
            if ele >= 1:
                return 1, arr_sum - 1

    mid_height = range / 2
    seq = [i for i in xrange(1, mid_height + 1)]
    seq1 = seq + [(range + 1) / 2]
    s1 = sum(seq) * 2 + seq1[-1]
    l = len(seq1)

    costs1 = linear_check(arr, seq1, l, n)
    costs2 = linear_check(arr[::-1], seq1, l, n)

    for i in xrange(n):
        if costs1[i] == 1 and costs2[n - i - 1] == 1:
            return 1, arr_sum - s1

    return 0, 2


def bs(arr, n, h, arr_sum):
    l = 1
    r = h + 1
    while r - l > 1:
        mid = (l + r) / 2
        #print h[mid]
        c = is_possbile(arr, 2 * mid - 1, n, arr_sum)
        if c[0]:
            l = mid
        else:
            r = mid
    #print h[l]
    return is_possbile(arr, 2 * l - 1, n, arr_sum)[1]

t1 = time()

t = input()
#t = 10
for a0 in xrange(t):
    n = input()
    arr = map(int, raw_input().split())
    #n = 10 ** 5

    #arr = [randrange(1, 10 ** 9) for i in xrange(n)]

    if n % 2 == 0:
        h = n / 2
    else:
        h = n / 2 + 1

    arr_sum = sum(arr)

    #print h
    print bs(arr, n, h, arr_sum)

#print time() - t1
