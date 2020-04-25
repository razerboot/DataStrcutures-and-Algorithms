t = input()
for a0 in xrange(t):
    n, q = map(int, raw_input().split())
    arr = map(int, raw_input().split())
    for a1 in xrange(q):
        a, b, c, d = map(int, raw_input().split())
        a, b, c, d = a - 1, b - 1, c - 1, d - 1
        arr1 = arr[a:b + 1]
        arr2 = arr[c:d + 1]
        #print arr1, arr2
        arr1.sort()
        arr2.sort()
        c = 0
        for i in xrange(b - a + 1):
            if arr1[i] != arr2[i]:
                if c == 1:
                    print 'NO'
                    break
                c += 1
        else:
            print 'YES'