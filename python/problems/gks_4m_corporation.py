def cal_ans(arr, ans):
    n = len(arr)
    if sum(arr) == n * ans[0]:
        if (n % 2 == 0 and (arr[n / 2] + arr[n / 2 - 1]) == 2 * ans[1]) or (n % 2 != 0 and arr[n / 2] == ans[1]):
            return 1
    return 0


def count_values(arr, i, n, ans):
    if i == n - 1:
        return cal_ans(arr, ans)

    for j in xrange(arr[i - 1], arr[-1] + 1):
        arr[i] = j
        if count_values(arr, i + 1, n, ans):
            return 1
        arr[i] = 0
    return 0

t = input()

for a0 in xrange(1, 1 + t):
    print 'Case #' + str(a0) + ':',
    mi, ma, m, M = map(int, raw_input().split())
    if mi > ma or m > ma or M > ma or m < mi or M < mi:
        print 'IMPOSSIBLE'
        continue
    if mi == ma == m == M:
        print 1
        continue
    ans = [m, M]
    for i in xrange(2, 14):
        l = i
        arr = [0] * i
        arr[0] = mi
        arr[-1] = ma
        if count_values(arr, 1, l, ans):
            print i
            break
    else:
        print 'IMPOSSIBLE'





