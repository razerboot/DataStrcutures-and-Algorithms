t = input()
mod = 64
powers = [1] * (mod + 1)
for i in xrange(1, mod + 1):
    powers[i] = 2 * powers[i - 1]

for a0 in xrange(t):
    n, k = map(int, raw_input().split())
    m = k / mod
    last = k % mod

    main_set = [0] * m
    for i in xrange(m):
        main_set[i] = powers[mod] - 1
    if last != 0:
        main_set.append(powers[last] - 1)
        m += 1

    arr = [0] * n
    for i in xrange(n):
        buff = [0] * m
        temp = map(int, raw_input().split())[1:]
        for ele in temp:
            ele -= 1
            q = ele / mod
            r = ele % mod
            buff[q] ^= powers[r]
        arr[i] = buff

    count = 0
    for i in xrange(n):
        for j in xrange(i + 1, n):
            for k in xrange(m):
                #bitwise or condition
                if arr[i][k] | arr[j][k] != main_set[k]:
                    break
            else:
                count += 1
    print count