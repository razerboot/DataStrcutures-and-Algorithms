t = input()
for a0 in xrange(t):
    n = input()
    arr = map(int, raw_input().split())
    arr.sort()
    p = n - 1 + (n + 1) / 2
    print arr[p]
    i = 0
    while 1:
        if i >= n:
            break
        print arr[i], arr[n + i],
        i += 1
    print
