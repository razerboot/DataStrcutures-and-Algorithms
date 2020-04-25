
def knight(N, M, x1, y1, x2, y2):
    from collections import deque, defaultdict
    moves = [(1, 2), (2, 1), (1, -2), (2, -1), (-1, -2), (-2, -1)]
    q = deque([(x1, y1)])
    vi = defaultdict(int)
    while 1:
        if len(q) == 0:
            return -1
        x = q.pop()
        if x == (x2, y2):
            return vi[x]
        for move in moves:
            new_x = x[0] + move[0]
            new_y = x[1] + move[1]
            if check(new_x, new_y, N, M, vi):
                vi[(new_x, new_y)] = vi[x] + 1
                q.appendleft((new_x, new_y))


def check(x, y, N, M, vi):
    if vi[(x, y)] == 0 and 1 <= x <= N and 1 <= y <= M:
        return True
    return False


print knight(8,8,1,1,8,8)