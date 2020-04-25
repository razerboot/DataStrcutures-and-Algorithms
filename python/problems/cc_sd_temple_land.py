def check_order(arr, n):
    l = 1
    for i in xrange(n):
        if arr[i] != l:
            return 'no'
        if i < (n - 1) / 2:
            l += 1
        else:
            l -= 1
    return 'yes'


q = input()
for _ in xrange(q):
    n = input()
    arr = map(int, raw_input().split())
    if n % 2 == 0 or arr[0] != 1 or arr[-1] != 1:
        print 'no'
    else:
        print check_order(arr, n)