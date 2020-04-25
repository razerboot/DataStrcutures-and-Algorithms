arr = map(int, raw_input().split(', '))
#print arr
n = len(arr)
dp = [[1, 1] for i in xrange(n)]
maxi = 1
for i in xrange(1, n):
    for j in xrange(i):
        # seq with ith value at high position
        if arr[i] > arr[j]: dp[i][1] = max(dp[i][1], dp[j][0] + 1)
        # seq with ith value at low position
        elif arr[i] < arr[j]: dp[i][0] = max(dp[i][0], dp[j][1] + 1)

    maxi = max(max(dp[i][0], dp[i][1]), maxi)

print maxi



