from collections import deque
import profile

class Line():
    '''line with slope m and constant c'''

    def __init__(self, c, m):
        self.m = m
        self.c = c
        self.left = None
        self.right = None

    def solve_x(self, x):
        return self.m * x + self.c

class Dll():
    '''dll for appending and popping left and right'''
    def __init__(self):
        self.lhead = None
        self.rhead = None

    def append_left(self,line):
        if self.lhead == None and self.rhead == None:
            self.lhead = line
            self.rhead = line
        else:
            line.right = self.lhead
            self.lhead.left = line
            self.lhead = line

    def append_right(self,line):
        if self.lhead == None and self.rhead == None:
            self.lhead = line
            self.rhead = line
        else:
            line.left = self.rhead
            self.rhead.right = line
            self.rhead = line

    def check_size(self):
        return self.lhead != self.rhead

    def pop_left(self):
        '''assuming popping is happening when length is atleast 2'''
        self.lhead = self.lhead.right


    def pop_right(self):
        self.rhead = self.rhead.left


def can_consume(l1, l2, l3):
    '''checking whether intersection of l3 and l1 is right to l1 and l2 that is x12-x13<=0 '''
    return (l1.c - l2.c) * (l3.m - l1.m) - (l1.c - l3.c) * (l2.m - l1.m) <= 0


def insert(lines, l3):
    '''inserting line and removing all lines consumed by it'''
    # l1=lines[1]
    # l2=lines[0]
    while lines.check_size() and can_consume(lines.lhead.right, lines.lhead, l3):
        lines.pop_left()
    lines.append_left(l3)


def query(lines, x):
    '''since x or altitude value is strictly decreasing we can pop lines to right from line
    where x has min y'''
    #print lines.lhead.m
    #print lines.rhead.m
    while lines.check_size() and lines.rhead.solve_x(x) > lines.rhead.left.solve_x(x):
        lines.pop_right()
    return lines.rhead.solve_x(x)

def iteration(N, k, weights_prod, weights_sum, heights, matrix1, matrix2, f):
    for i in xrange(2, k + 1):
        lines = Dll()
        lines.append_left(Line(- 1 * weights_prod[i - 1], weights_sum[i - 1]))
        for j in xrange(i + 1, N + 1):
            lines.append_left(Line(matrix1[j - 1] - weights_prod[j - 1], weights_sum[j - 1]))
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

profile.run('iteration(N, k, weights_prod, weights_sum, heights, matrix1, matrix2, f)', sort='tottime')



