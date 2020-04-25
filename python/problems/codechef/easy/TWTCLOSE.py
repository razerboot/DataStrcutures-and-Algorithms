# problem - https://www.codechef.com/problems/TWTCLOSE

n, k = map(int, raw_input().split())
s = set()
for a0 in xrange(k):
    inp = raw_input().split()
    if len(inp) > 1:
        v = int(inp[1])
        if v in s:
            s.remove(v)
        else:
            s.add(v)
    else:
        s.clear()
    print len(s)
