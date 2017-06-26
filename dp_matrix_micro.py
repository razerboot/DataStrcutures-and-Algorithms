import sys


def dp(n):
    a = []
    for i in xrange(n):
        a.append(map(int, raw_input().split()))
    v = {}
    for i in xrange(n):
        for j in xrange(n):
            if i + 1 < n and a[i][j] == a[i + 1][j]:
                v[(i, j)] = [1]
            else:
                v[(i, j)] = [0]
            if j + 1 < n and a[i][j] == a[i][j + 1]:
                v[(i, j)].append(1)
            else:
                v[(i, j)].append(0)
    for l in xrange(2, n + 1):
        c = 0
        for i in xrange(n - l + 1):
            for j in xrange(n - l + 1):
                if l == 2:
                    if v[(i, j)] == [1, 1] and v[(i, j + 1)][0] == 1:
                        v[(i, j)].append(1)
                        c += 1
                    else:
                        v[(i, j)].append(0)
                else:
                    if v[(i, j)][l - 1] == 1 and v[(i + 1, j)][l - 1] == 1 and v[(i, j + 1)][l - 1] == 1:
                        v[(i, j)].append(1)
                        c += 1
                    else:
                        v[(i, j)].append(0)
        if c == 0:
            return l - 1
    return l


t = input()
for x in xrange(t):
    n = input()
    print dp(n)

