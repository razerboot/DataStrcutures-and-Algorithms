def compare(temp):
    c = 1
    maxi = 1
    n = len(temp)
    for i in xrange(n - 1):
        if temp[i] == temp[i + 1]:
            c += 1
        else:
            c = 1
        maxi = max(maxi, c)
    return maxi

t = input()
for x in xrange(t):
    mat = []
    max_j = 0
    max_i = 0
    n, m = map(int, raw_input().split())
    for y in xrange(n):
        temp = map(int, raw_input().split())
        max_j = max(max_j, compare(temp))
        mat.append(temp)
    for y in xrange(m):
        temp = []
        for z in xrange(n):
            temp.append(mat[z][y])
        max_i = max(max_i, compare(temp))
    print max_i * max_j

