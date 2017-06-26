def left_of_val(a, val, n):
    l = -1
    r = n
    while r - l > 1:
        mid = (l + r) / 2
        if a[mid] >= val:
            r = mid
        else:
            l = mid
    return r


t = input()
for a0 in xrange(t):
    n = input()
    a = map(int, raw_input().split())
    a.sort()
    i = left_of_val(a, 0, n)
    #print i
    if a[0] >= 0:
        print sum(a) * n
    elif a[-1] <= 0:
        print sum(a)
    else:
        s = sum(a[i:])
        n1 = len(a[i:])
        while i > 0 and (s + a[i - 1]) * (n1 + 1) >= s * n1:
            i -= 1
            n1 += 1
            s += a[i]
        #print i, n1, s
        print sum(a[:i]) + s * n1
