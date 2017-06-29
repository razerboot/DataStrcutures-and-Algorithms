def is_not_prefix(P, suffix, k, l):
    # an empty string is a prefix of any string
    if k <= -1:
        return 0
    for i in xrange(k + 1):
        if P[k - i] != suffix[l - i - 1]:
            return 1
    return 0


def preprocess(P):
    m = len(P)
    inp = ['a', 'b', 'c']
    states = [[0] * len(inp) for i in xrange(m + 1)]
    for i in xrange(m + 1):
        for j in xrange(len(inp)):
            suffix = ''
            if i > 0:
                suffix = P[:i]
            suffix += inp[j]
            k = min(i, m - 1)
            while is_not_prefix(P, suffix, k, i + 1):
                k -= 1
            states[i][j] = k + 1

    return states


def find_pattern(T, P, states):
    s = 0
    c = 0
    n = len(T)
    m = len(P)
    for i in xrange(n):
        s = states[s][ord(T[i]) - 97]
        if s == m:
            c += 1
    print c
P = 'aabab'
states = preprocess(P)
print states
find_pattern('aaababaabaababaab', P, states)