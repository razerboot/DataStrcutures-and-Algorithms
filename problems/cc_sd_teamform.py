t = input()
for a0 in xrange(t):
    n, m = map(int, raw_input().split())
    for a1 in xrange(m):
        b = raw_input()
    if (n - 2 * m) % 2 == 0:
        print 'yes'
    else:
        print 'no'