def direc(x, y, p, n, m, arr):
    for ele in p:
        if 1 <= x + ele[0] <= n and 1 <= y + ele[1] <= m and arr[x + ele[0]][y + ele[1]] == 0:
            return True, ele
    return False, (1, 2)


t = input()
p = [(0, 1), (0, -1), (1, 0), (-1, 0)]
out = {}
out[p[0]] = "Right"
out[p[1]] = "Left"
out[p[2]] = "Front"
out[p[3]] = "Back"
for x in xrange(t):
    n, m = map(int, raw_input().split())
    arr = [[0 for j in xrange(m + 1)] for i in xrange(n + 1)]
    s = map(int, raw_input().split())
    d = map(int, raw_input().split())
    if s == d:
        if s[1] == 1:
            print "Right"
        else:
            print "Left"
        continue
    arr[s[0]][s[1]]=1
    while 1:
        sd = direc(s[0], s[1], p, n, m, arr)
        if s == d:
            print arr
            if sd[0]:
                print out[sd[1]]
                break
            else:
                print "Over"
                break
        if sd[0]:
            print out[sd[1]]
            s[0] += sd[1][0]
            s[1] += sd[1][1]
            arr[s[0]][s[1]] = 1







