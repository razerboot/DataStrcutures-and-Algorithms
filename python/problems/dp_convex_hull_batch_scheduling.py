from collections import deque


class Line():

    def __init__(self, c, m):
        self.c = c
        self.m = m

    def solve_x(self, x):
        return self.m * x + self.c

def can_consume(l1, l2, l3):
    '''checking whether intersection of l3 and l1 is left to l1 and l2 that is x12-x13<=0 '''
    return (l1.c - l2.c) * (l3.m - l1.m) - (l1.c - l3.c) * (l2.m - l1.m) >= 0

def insert(lines, l3):
    while len(lines) > 1 and can_consume(lines[-2], lines[-1], l3):
        lines.pop()
    lines.append(l3)

def query(lines, x):
    # since x is increasing checking from left removing lines from left
    while len(lines) > 1 and lines[0].solve_x(x) > lines[1].solve_x(x):
        lines.popleft()
    return lines[0].solve_x(x)
#input

N = input()
s = input()
T = [0] * (N + 1)
F = [0] * (N + 1)
for a0 in xrange(1, N + 1):
    t, f = map(int, raw_input().split())
    T[a0], F[a0] = t, f

#preprocessing
F_suffix_sum = [0] * (N + 1)
T_suffix_sum = [0] * (N + 1)
F_suffix_sum[N], T_suffix_sum[N] = F[N], T[N]
for a0 in reversed(xrange(1, N)):
    F_suffix_sum[a0] = F_suffix_sum[a0 + 1] + F[a0]
    T_suffix_sum[a0] = T_suffix_sum[a0 + 1] + T[a0]

cost = [0] * (N + 1)
cost[N] = F[N] * (T[N] + s)
lines = deque([])
lines.append(Line(cost[N], -1 * T[N]))

for k in reversed(xrange(1,N)):
    #cost for full batch from k to N without splits
    c = (s + T_suffix_sum[k]) * F_suffix_sum[k]
    #print c
    cost[k] = min(c, c + query(lines, F_suffix_sum[k]))
    insert(lines, Line(cost[k], -1 * T_suffix_sum[k]))

print cost[1]

