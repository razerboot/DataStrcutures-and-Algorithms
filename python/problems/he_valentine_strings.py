
t = input()
for a0 in xrange(t):
    n = input()
    arr = []
    for a1 in xrange(n):
        temp = set(raw_input())
        arr.append(temp)
    counts = [0] * 101
    for i in xrange(n):
        for j in xrange(i + 1, n):
            counts[len(arr[i] & arr[j])] += 1

    suffix_counts = [0] * 101
    suffix_counts[100] = counts[100]
    for i in reversed(xrange(100)):
        suffix_counts[i] = suffix_counts[i + 1] + counts[i]

    q = input()
    for a2 in xrange(q):
        k = input()
        if k > 100:
            print 0
        else:
            print suffix_counts[k]