from random import randrange
from time import time


def ceil(arr, k, n):
    '''finding left index to ceiling position'''
    l = -1
    r = n
    while r - l > 1:
        mid = (l + r) / 2
        if arr[mid] >= k:
            r = mid
        else:
            l = mid
    return l


def left_to_val(arr, val, left, right):
    '''finding left extreme of val(repeated)'''
    l = left
    r = right
    while r - l > 1:
        mid = (l + r) / 2
        if arr[mid] >= val:
            r = mid
        else:
            l = mid
    return r


def remaining_snakes(arr, key, k):
    '''for remaining snakes with length less than k from highest length snake,
    eating snakes from left till its length reaches k'''
    l = 0
    r = key
    count = 0
    while l < r:

        l_index = left_to_val(arr, arr[r], l - 1, r)
        c = r - l_index + 1
        c1 = k - arr[r]
        const = c * c1

        if const < l_index - l:
            count += c
            l += const
            r = l_index - 1

        elif const == l_index - l:
            count += c
            return count

        else:
            count += (r - l + 1) / (1 + c1)
            return count

    return count


def main_function():
    #t = input()
    t = 5
    for a0 in xrange(t):
        #n, q = map(int, raw_input().split())
        n, q = 10 ** 5, 10 ** 5
        arr = [randrange(1, 10 ** 7) for i in xrange(n)]
        #arr = map(int, raw_input().split())
        arr.sort()

        for a1 in xrange(q):
            count = 0
            #k = input()
            k = randrange(10 ** 6, 10 ** 9)
            #k = 101010102
            key = ceil(arr, k, n)
            count += n - key - 1
            if key == -1:
                count = count
            else:
                count += remaining_snakes(arr, key, k)
            #print count

t1 = time()
main_function()
print time() - t1