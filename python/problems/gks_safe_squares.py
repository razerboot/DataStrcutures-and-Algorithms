from time import time

t = input()
for a0 in xrange(t):
    n, m, K = map(int, raw_input().split())
    monsters = set([])
    for a1 in xrange(K):
        i, j = map(int, raw_input().split())
        monsters.add((i, j))
    dp = [[0 for j in xrange(m)] for i in xrange(n)]
    safe_squares = 0
    for i in reversed(xrange(n)):
        for j in reversed(xrange(m)):
            if (i, j) in monsters: continue
            if j == m - 1 or i == n - 1: dp[i][j] = 1
            else:
                dp[i][j] = min(dp[i][j + 1], dp[i + 1][j], dp[i + 1][j + 1]) + 1
            safe_squares += dp[i][j]
    print 'Case #' + str(a0 + 1) + ':',
    print safe_squares

#print time() - t1