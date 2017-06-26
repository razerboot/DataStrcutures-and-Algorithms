#calculate phi for the pattern p (phi is proper prefix of pattern that is suffix with length strictly less than the pattern)
def compute_prefix_function(P, m):
    phi = [0] * (1 + m)
    k = 0
    for i in xrange(2, m + 1):
        while k > 0 and P[k + 1] != P[i]:
            k = phi[k]
        if P[k + 1] == P[i]:
            k += 1
        phi[i] = k
    return phi


def kmp(T, P):
    n, m = len(T), len(P)
    P, T = ' ' + P, ' ' + T
    phi = compute_prefix_function(P, m)
    # no of matched characters
    q = 0
    for i in xrange(1, n + 1):
        while q > 0 and P[q + 1] != T[i]:
            q = phi[q]
        if P[q + 1] == T[i]:
            q += 1
        if q == m:
            print 'match found'
            print i - m + 1
            q = phi[q]

kmp("AABAACAABAAAAAABAACAABAACAABAACAABAA", "AABAACAABAA")


