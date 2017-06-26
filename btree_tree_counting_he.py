# from collections import defaultdict
def traversal(A, node, tree, childMap, count, n, k):
    childs = []
    if node not in tree:
        childMap[node] = []
        return
    for child in tree[node]:
        traversal(A, child, tree, childMap, count, n, k)
        childs += [child] + childMap[child]
    childMap[node] = childs
    count[0] += count_k(k, A, node, childs)


def count_k(k, A, node, childs):
    k -= A[node]
    n = len(childs)
    if k <= 0:
        return n * (n - 1) / 2
    scores = []
    for child in childs:
        scores.append(A[child])
    scores.sort()
    return get_count(n, scores, k)


def get_count(n, scores, k):
    i = 0
    j = n - 1
    count = 0
    while (i <= j):
        if scores[i] + scores[j] >= k:
            count += j - i
            j -= 1
        else:
            i += 1
    return count


n, k = map(int, raw_input().split())
A = [0]+list(map(int, raw_input().split()))
data = map(int, raw_input().split())

tree = {}
childMap = {}
count = [0]
for a0 in xrange(2, n + 1):
    parent = data[a0 - 2]
    if parent in tree:
        tree[parent].add(a0)
    else:
        tree[parent] = set([a0])
traversal(A, 1, tree, childMap, count, n, k)

print count
