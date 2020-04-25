from math import log,ceil


def fill_heap(index, heap, N):
    if index >= N:
        return

    if heap[index] == -1:
        l = 2 * index + 1
        r = 2 * index + 2

        if l < N:
            if heap[l] == -1:
                fill_heap(l, heap, N)
            if heap[l] != -1:
                heap[index] = heap[l]

        if r < N:
            if heap[r] == -1:
                fill_heap(r, heap, N)
            if heap[r] != -1:
                if heap[index] == -1 or heap[index][1] < heap[r][1]:
                    heap[index] = heap[r]


def replace(r, heap):
    p1 = (r - 1)/2
    l1 = 2 * p1 + 1
    r1 = 2 * p1 + 2
    if heap[r1] == -1 or heap[r1][1] <= heap[l1][1]:
        heap[p1] = heap[l1]
    elif heap[l1] == -1 or heap[l1][1] < heap[r1][1]:
        heap[p1] = heap[r1]
    if p1 > 0:
        replace(p1, heap)

n, k, p = map(int, raw_input().split())
arr = map(int, raw_input().split())
if k < n:
    sum_array = [0] * n
    sum_array[0] = sum(arr[:k])
    for i in xrange(1, n):
        sum_array[i] = sum_array[i - 1] - arr[i - 1] + arr[(i + k - 1) % n]

    c = 2 ** (int(ceil(log(n - k + 1, 2))))
    N = 2 * c - 1

    heap = [-1] * N
    for i in xrange(n - k + 1):
        heap[c - 1 + i] = (i, sum_array[i])
    #print sum_array
    fill_heap(0, heap, N)
    #print heap
    maxi_array = [0] * n
    maxi_array[0] = heap[0][1]

    for i in xrange(1, n):
        r = (i + n - k) % (n - k + 1)
        heap[c - 1 + r] = (r, sum_array[(i + n - k) % n])
        #print heap
        const = [0]
        replace(c - 1 + r, heap)
        #print heap
        #print
        maxi_array[i] = heap[0][1]
    c1 = 0
    c2 = 0
    query = raw_input()
    for q in query:
        if q == '?':
            print maxi_array[c2]
        elif q == '!':
            c1 += 1
            c2 = n - c1 % n
            if c2 == n:
                c2 = 0

else:
    query = raw_input()
    c1 = sum(arr)
    for q in query:
        if q == '?':
            print c1