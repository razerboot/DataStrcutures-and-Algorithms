t = input()
for a0 in xrange(t):
    u, v = map(int, raw_input().split())
    t = u + v
    print (t * (t + 1) / 2) + u + 1