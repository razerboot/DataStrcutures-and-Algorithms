def find_anagram(s, c, n, out, l, fact):
    if c == 0:
        out.extend(s)
        return
    i = c / fact[l]
    r = c % fact[l]
    out.append(s.pop(i))
    find_anagram(s, r, n, out, l - 1, fact)

fact = [1] * 20
for i in xrange(1, 20):
    fact[i] = i * fact[i - 1]
t = input()
for a0 in xrange(t):
    s, c = raw_input().split()
    s = list(s)
    n = len(s)
    c = int(c)
    c -= 1
    s.sort()
    out = []
    find_anagram(s, c, n, out, n - 1, fact)
    print ''.join(out)
