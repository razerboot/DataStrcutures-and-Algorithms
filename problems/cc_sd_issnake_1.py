from collections import defaultdict, deque


def bfs(x, rows, edges):
    '''for finding all pair shortest paths'''
    q = deque([x])
    vi = defaultdict(int)
    vi[x] = 1
    while len(q) > 0:
        u = q.pop()
        for di, dj in edges:
            v = u[0] + di, u[1] + dj
            if (v[0] == 0 or v[0] == 1) and (0 <= v[1] < n) and rows[v[0]][v[1]] == '#' and vi[v] == 0:
                q.appendleft(v)
                vi[v] = 1
    return vi


t = input()

edges = [(1, 0), (0, 1), (-1, 0), (0, -1)]

for a0 in xrange(t):
    n = input()
    node = None
    n1 = 0
    rows = [raw_input() for i in xrange(2)]
    for j in xrange(n):
        if rows[0][j] == '#':
            if node is None:
                node = 0, j
            n1 += 1
        if rows[1][j] == '#':
            if node is None:
                node = 1, j
            n1 += 1
    #print graph
    #print degree
    #print n1
    if n1 == 1:
        print 'yes'
        continue
    vi = bfs(node, rows, edges)
    vi_count = 0
    for node in vi:
        if vi[node] == 1:
            vi_count += 1
    #print vi_count
    if vi_count < n1:
        print 'no'
        continue

    block_length = 0
    start = 0
    flag = 0
    for j in xrange(n):
        if rows[0][j] == '#' and rows[1][j] == '#':
            if flag == 0:
                flag = 1
                block_length = 1
                start = j
            else:
                block_length += 1
        elif rows[0][j] == '#' or rows[1][j] == '#':
            if flag == 1:
                if block_length % 2 == 0:
                    if start != 0:
                        if (rows[0][j] == '#' and rows[1][start - 1] == '#') or (rows[1][j] == '#' and rows[0][start - 1] == '#'):
                            print 'no'
                            break
                else:
                    if start != 0:
                        if (rows[0][j] == '#' and rows[0][start - 1] == '#') or (rows[1][j] == '#' and rows[1][start - 1] == '#'):
                            print 'no'
                            break
                flag = 0
    else:
        print 'yes'

