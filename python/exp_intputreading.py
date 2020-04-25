from collections import defaultdict, deque

n = input()


def flip(i, a, n):
    i1 = i-1
    i2 = (i) % n
    i3 = (i+1) % n
    j = 0
    num = []
    for ele in a:
        if i1 == j or i2 == j or i3 == j:
            num.append(ele ^ 1)
        else:
            num.append(ele)
        j += 1
    return tuple(num)


def bfs(u, v, n):
    c = defaultdict(int)
    q = deque([u])
    c[u] = 1
    while (len(q) > 0):
        a = q.pop()
        if a == v:
            return c[a] - 1
        for i in range(1, n + 1):
            new_i = flip(i, a,n)
            if c[new_i] == 0:
                q.appendleft(new_i)
                c[new_i] = c[a] + 1

    return "Impossible"


u = tuple(map(int, raw_input().split()))
v = tuple(map(int, raw_input().split()))

print bfs(u, v, n)
