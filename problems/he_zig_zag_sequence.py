def dp(arr, n):
    max_seq_arr = [0] * n
    for i in xrange(n):
        if i == 0:
            max_seq_arr[i] = arr[i]
        else:
            maxi = arr[i]
            for j in xrange(i):
                if arr[i]>arr[j] and maxi < arr[i] + max_seq_arr[j]:
                    maxi = arr[i] + max_seq_arr[j]
            max_seq_arr[i] = maxi
    return max_seq_arr

t = input()
for a0 in xrange(t):
    n = input()
    arr = map(int, raw_input().split())
    max_left = dp(arr, n)
    max_right = dp(arr[::-1], n)[::-1]

    index = -1
    maxi = None
    for i in xrange(n):
        if maxi is None or maxi < max_left[i] + max_right[i] - arr[i]:
            maxi = max_left[i] + max_right[i] - arr[i]
            index = i

    print maxi, arr[index]