# solving magical thinking in O(q) time complexity
# first compare friend 1 and friend 2 answers and find k1 and k2
# divide the problem into 2 sub-problems of size x1, y1
# where x1 is size of list friend 1 and friend 2 agrees, y1 relates to friend1 disagrees with friend 2
# 0 <= k1 <= x1, 0 <= k2 <= y1, s1, s2, scores of friend1 and friend2
# k1 + k2 = s1, k1 + y1 - k2 = s2 from these equation we can find both k1, k2


def find_max_count(u, v, q, sv):
    x, y = 0, 0
    for i in xrange(q):
        if u[i] == v[i]:
            x += 1
        else:
            y += 1
    if sv == x:
        return q
    elif sv < x:
        return y + sv
    else:
        return x + q - sv

t = input()
for a0 in xrange(1, 1 + t):
    print 'Case #' + str(a0) + ':',
    n, q = map(int, raw_input().split())
    if n == 1:
        v1 = raw_input()
        u = raw_input()
        s1 = input()
        print find_max_count(u, v1, q, s1)
    else:
        v1 = raw_input()
        v2 = raw_input()
        u = raw_input()
        s1, s2 = map(int, raw_input().split())
        y1 = 0
        v1x, v1y, ux, uy = [], [], [], []
        for i in xrange(q):
            if v1[i] != v2[i]:
                v1y.append(v1[i])
                uy.append(u[i])
                y1 += 1
            else:
                v1x.append(v1[i])
                ux.append(u[i])
        k1 = (s1 + s2 - y1) / 2
        k2 = (s1 - s2 + y1) / 2
        print find_max_count(ux, v1x, len(ux), k1) + find_max_count(uy, v1y, len(uy), k2)


