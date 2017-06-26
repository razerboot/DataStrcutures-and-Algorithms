from collections import deque
from random import randrange
from time import time


def bfs(a, distances, q, edges, n, m):

    maxi = -1
    #finding max value in the matrix
    for i in xrange(n):
        for j in xrange(m):
            maxi = max(maxi, a[i][j])

    # finding i, j where a[i][j] is max and adding them to queue and intializing distance as zero
    for i in xrange(n):
        for j in xrange(m):
            if a[i][j] == maxi:
                q.append((i, j))
                distances[i][j] = 0
            else:
                distances[i][j] = -1

    # bfs and updating distances of each node till q is empty
    max_distance = 0
    while len(q) > 0:
        x, y = q.pop()
        for (dx, dy) in edges:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and distances[nx][ny] == -1:
                q.appendleft((nx, ny))
                distances[nx][ny] = distances[x][y] + 1
                if distances[nx][ny] > max_distance:
                    max_distance = distances[nx][ny]

    return max_distance

t1 = time()
# edges for each node in matrix
edges = [(1, 0), (0, 1), (1, 1), (-1, -1), (-1, 1), (-1, 0), (0, -1), (1, -1)]
t = raw_input().strip()
t = int(t)


distances = [[0 for j in xrange(500)] for i in xrange(500)]
a = [[0 for j in xrange(500)] for i in xrange(500)]

# q used for bfs
q = deque([])

for a0 in xrange(t):
    n, m = map(int, raw_input().strip().split())
    #n, m = 500, 500
    for i in xrange(n):
        temp = map(int, raw_input().strip().split())
        #temp = [randrange(500000,1000001) for j in xrange(m)]
        for j in xrange(m):
            a[i][j] = temp[j]
    q.clear()
    print bfs(a, distances, q, edges, n, m)

#print time() - t1