

def traverse(arr, n):

    # row wise checking for each row with at most 2 X's
    for i in xrange(n):
        c = 0
        for j in xrange(n):
            if arr[i][j] == 'X':
                c += 1
        if c == 0 or c > 2:
            return 0

    # column wise checking for each column with at most 2 X's
    for j in xrange(n):
        c = 0
        for i in xrange(n):
            if arr[i][j] == 'X':
                c += 1
        if c == 0 or c > 2:
            return 0

    # checking no of rectangles is equal to n - 1 / 2
    # and single X
    rectangle_count = 0
    s = set([])
    for i in xrange(n):
        if arr[i] not in s:
            s.add(arr[i])
        else:
            s.remove(arr[i])
            rectangle_count += 1

    if len(s) == 0 or len(s) > 1 or rectangle_count != (n - 1) / 2:
        return 0
    ele, = s
    c = 0
    for i in xrange(n):
        if ele[i] == 'X':
            c += 1
    if c == 0 or c > 1:
        return 0

    return 1


t = input()
for a0 in xrange(1, t + 1):
    print 'Case #' + str(a0) + ':',
    n = input()
    arr = []
    for a1 in xrange(n):
        arr.append(raw_input())
    ans = traverse(arr, n)
    if ans:
        print 'POSSIBLE'
    else:
        print 'IMPOSSIBLE'

