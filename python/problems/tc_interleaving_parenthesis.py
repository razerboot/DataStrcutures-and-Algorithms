s1 = raw_input()
s2 = raw_input()
n = len(s1)
m = len(s2)
mod = 10 ** 9 + 7

A = [0] * (n + 1)
B = [0] * (m + 1)
for i in xrange(1, n + 1):
    if s1[i - 1] == '(': A[i] = A[i - 1] + 1
    else: A[i] = A[i - 1] - 1

for j in xrange(1, m + 1):
    if s2[j - 1] == '(': B[j] = B[j - 1] + 1
    else: B[j] = B[j - 1] - 1

dp = [[0 for j in xrange(m + 1)] for i in xrange(n + 1)]
dp[0][0] = 1
for i in xrange(n + 1):
    for j in xrange(m + 1):
        if i == 0 and j == 0:
            continue
        if j: dp[i][j] = dp[i][j - 1]
        if i: dp[i][j] = (dp[i][j] + dp[i - 1][j]) % mod
        if A[i] + B[j] < 0: dp[i][j] = 0

#print A, B
#print dp

if A[n] + B[m] == 0:
    print dp[n][m]
else:
    print 0