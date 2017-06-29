#this code works for commutative combiner function(ex : min(a, b) = min(b, a))
# and range query and single element modification


def f(x, y):
    return min(x, y)


def build(seg_tree, n):
    for i in reversed(xrange(1, n)):
        seg_tree[i] = f(seg_tree[2 * i], seg_tree[2 * i + 1])


def modify(seg_tree, p, val, n):
    p += n
    seg_tree[p] = val
    while p > 1:
        # p / 2 is parent, p is self, p ^ 1 is other child (p ^ 1 turns even to odd, odd to even)
        seg_tree[p / 2] = f(seg_tree[p], seg_tree[p ^ 1])
        p /= 2


def query(seg_tree, l, r, n):
    #l and r inclusive
    res = float('inf')
    l, r = l + n, r + n
    while l <= r:
        #if l is odd then its parent is not included so we have to include this when visiting left borders
        if l % 2 != 0:
            res = f(res, seg_tree[l])
            l += 1
        #if r is even then its parent is not included so we have to include this when visiting right borders
        if r % 2 == 0:
            res = f(res, seg_tree[r])
            r -= 1
        if l == r:
            break
        l, r = l / 2, r / 2
    return res


n, q = map(int, raw_input().split())
arr = map(int, raw_input().split())
# size of segment tree is 2 * n - 1(using perfect binary tree)
#since using 1 based index for tree total 2 * n elements
seg_tree = [-1] * (2 * n)
for i in xrange(n):
    seg_tree[n + i] = arr[i]

build(seg_tree, n)
#print seg_tree
for i in xrange(q):
    t, x, y = raw_input().split()
    x, y = int(x), int(y)
    if t == 'q':
        print query(seg_tree, x - 1, y - 1, n)
    else:
        modify(seg_tree, x - 1, y, n)