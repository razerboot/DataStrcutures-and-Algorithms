t = int(raw_input().strip())
for a0 in xrange(1, t + 1):
    signs = raw_input().strip()
    maxi = 0
    arr = []
    n = len(signs)
    curr, count = '', 0
    for i in xrange(n):
        if signs[i] == '=':
            continue
        if curr == '':
            curr = signs[i]
            count = 1
        else:
            if curr != signs[i]:
                arr.append((curr, count))
                curr, count = signs[i], 1
            else:
                count += 1
    if curr != '':
        arr.append((curr, count))
    n = len(arr)
    if n == 0:
        print 1
        continue
    arr1 = [0] * (n + 1)
    if arr[0][0] == '<':
        arr1[0] = 1
        arr1[1] = arr[0][1] + 1
    if arr[-1][0] == '>':
        arr1[-1] = 1
        arr1[-2] = max(arr1[-2], arr[-1][1] + 1)
    for i in xrange(1, n):
        if arr[i - 1][0] == '>' and arr[i][0] == '<':
            arr1[i] = 1
            arr1[i - 1] = max(arr1[i - 1], arr[i - 1][1] + 1)
            arr1[i + 1] = max(arr1[i + 1], arr[i][1] + 1)
    print max(arr1)
