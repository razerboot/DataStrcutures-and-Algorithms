import heapq
from blist import *

n = input()
entry = {}
get = arr.get
# min_heap = []
heap = SortedList()
length = 0
while (n > 0):
    junk = raw_input().split(' ')
    t = int(junk[0])
    if len(junk) > 1:
        v = int(junk[1])
    if t == 1:
        k = get(v, None)
        if k:
            arr[v] += 1
        else:
            arr[v] = 1
            heap.add(v)
            # push to min_heap and max_heap
        length += 1
    elif t == 2:
        k = get(v, None)
        if k and k == 1:
            heap.remove(v)
            del arr[v]
            length -= 1
        elif k and k > 1:
            arr[v] -= 1
            length -= 1
        else:
            print -1
    elif t == 3:
        if length == 0:
            print -1
        else:
            print heap[-1]
    elif t == 4:
        if length == 0:
            print -1
        else:
            print heap[0]

    n -= 1