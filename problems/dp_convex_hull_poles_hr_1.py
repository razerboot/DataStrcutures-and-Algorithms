import profile
from collections import deque


class Line():
    '''line with slope m and constant c'''

    def __init__(self, c, m):
        self.m = m
        self.c = c

    def solve_x(self, x):
        return self.m * x + self.c


def can_consume(l1, l2, l3):
    '''checking whether intersection of l3 and l1 is right to l1 and l2 that is x12-x13<=0 '''
    return (l1.c - l2.c) * (l3.m - l1.m) - (l1.c - l3.c) * (l2.m - l1.m) <= 0


def insert(lines, l3):
    '''inserting line and removing all lines consumed by it'''
    # l1=lines[1]
    # l2=lines[0]
    while (len(lines) > 1 and can_consume(lines[1], lines[0], l3)):
        lines.popleft()
    lines.appendleft(l3)


def query(lines, x):
    '''since x or altitude value is strictly decreasing we can pop lines to right from line
    where x has min y'''
    while (len(lines) > 1 and lines[-1].solve_x(x) > lines[-2].solve_x(x)):
        lines.pop()
    # print lines
    return lines[-1].solve_x(x)


def iteration(N, k, weights_prod, weights_sum, heights, matrix1, matrix2, f):
    for i in xrange(2, k + 1):
        lines = deque([])
        lines.append(Line(- 1 * weights_prod[i - 1], weights_sum[i - 1]))
        for j in xrange(i + 1, N + 1):
            insert(lines, Line(matrix1[j - 1] - weights_prod[j - 1], weights_sum[j - 1]))
            matrix2[j] = f[j] + query(lines, heights[j])
        matrix1, matrix2 = matrix2, matrix1

    print matrix1[N]


# input
N, k = map(int, raw_input().split())
weights = [0] * (N + 1)
heights = [0] * (N + 1)
for a0 in reversed(xrange(1, N + 1)):
    h, w = map(int, raw_input().split())
    weights[a0] = w
    heights[a0] = h

# preprocessing weight and weight*height matrix
weights_sum = [0] * (N + 1)
weights_prod = [0] * (N + 1)
f = [0 for j in xrange(N + 1)]
matrix1 = [0 for j in xrange(N + 1)]
matrix2 = [0 for j in xrange(N + 1)]

for j in xrange(1, N + 1):
    # preprocessing
    weights_sum[j] = weights_sum[j - 1] + weights[j]
    weights_prod[j] = weights_prod[j - 1] + weights[j] * heights[j]
    # base case
    matrix1[j] = weights_prod[j] - heights[j] * weights_sum[j]
    f[j]=matrix1[j]
iteration(N, k, weights_prod, weights_sum, heights, matrix1, matrix2, f)
#profile.run('iteration(N, k, weights_prod, weights_sum, heights, matrix1, matrix2, f)', sort='tottime')

