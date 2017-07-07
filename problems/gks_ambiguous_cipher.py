t = input()
for a0 in xrange(1, t + 1):
    print 'Case #' + str(a0) + ':',
    E = ' ' + raw_input()
    n = len(E) - 1
    D = [''] * (n + 1)
    if n % 2 != 0:
        # answer is ambiguous for odd length since we cant determine values at odd places
        print 'AMBIGUOUS'
        continue
    D[2] = E[1]
    D[-2] = E[-1]
    # solving for even places, 1 based indexing
    for i in xrange(4, n + 1, 2):
        val = ord(E[i - 1]) - ord(D[i - 2])
        if val >= 0:
            D[i] = chr(val + 65)
        else:
            D[i] = chr(val + 26 + 65)

    # solving for odd places, from right to left
    for i in reversed(xrange(1, n - 1, 2)):
        val = ord(E[i + 1]) - ord(D[i + 2])
        if val >= 0:
            D[i] = chr(val + 65)
        else:
            D[i] = chr(val + 26 + 65)

    print ''.join(D[1:])

