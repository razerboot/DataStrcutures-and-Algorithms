# classic interval problem technique where we can divide each interval into two
# parts (a, b) as (a, 'start', i) and (b, 'end', i) where i is the position of
# interval and sort them, and work on the sorted array for total area contribution
# and individual interval contribution to the total from left to right
from operator import itemgetter as it
from collections import defaultdict

t = input()
for a0 in xrange(1, t + 1):
    n, l1, r1, A, B, C1, C2, M = map(int, raw_input().split())

    marks = [(l1, r1, 1, 'start'), (r1, l1, 1, 'end')]
    xprev, yprev = l1, r1
    for i in xrange(2, n + 1):
        x, y = (A * xprev + B * yprev + C1) % M, (A * yprev + B * xprev + C2) % M
        marks.append((min(x, y), max(x, y), i, 'start'))
        marks.append((max(x, y), min(x, y), i, 'end'))
        xprev, yprev = x, y

    marks.sort(key=it(0))

    s = set([marks[0]])
    prev = marks[0]
    total_area = 0
    interval_area = defaultdict(int)

    for i in xrange(1, 2 * n):
        if len(s) > 0:
            area = 0
            if marks[i][3] == 'start' and prev[3] == 'start':
                area = marks[i][0] - prev[0]
            elif marks[i][3] == 'start' and prev[3] == 'end':
                area = marks[i][0] - prev[0] - 1
            elif marks[i][3] == 'end' and prev[3] == 'start':
                area = marks[i][0] - prev[0] + 1
            elif marks[i][3] == 'end' and prev[3] == 'end':
                area = marks[i][0] - prev[0]

            total_area += area

            if len(s) == 1:
                temp, = s
                interval_area[temp[2]] += area

        if marks[i][3] == 'start':
            s.add(marks[i])
        else:
            s.remove((marks[i][1], marks[i][0], marks[i][2], 'start'))

        prev = marks[i]

    print 'Case #' + str(a0) + ':',
    print total_area - max(interval_area.itervalues())

