def cal_cost(x, y, matrix):
    max_t = -1
    for x1, y1, x2, y2 in matrix:
        if x1 == x2 and y1 != y2:
            # vertical snake
            t = abs(x - x1)
            if y1 > y2:
                y1, y2 = y2, y1
            if y2 < y:
                #choosen point is right to the snake
                t += y - y2
            elif y < y1:
                # choosen point is left to the snake
                t += y1 - y

        elif x1 != x2 and y1 == y2:
            t = abs(y - y1)
            if x1 > x2:
                x1, x2 = x2, x1
            if x2 < x:
                t += x - x2
            elif x < x1:
                t += x1 - x

        elif x1 == x2 and y1 == y2:
            t = abs(x - x1) + abs(y - y1)

        max_t = max(max_t, t)
    return max_t


t = input()
for a0 in xrange(t):
    n = input()
    matrix = []
    for a1 in xrange(n):
        matrix.append(map(int, raw_input().split()))
    min_t = -1
    for i in xrange(1, 50):
        for j in xrange(1, 50):
            cost = cal_cost(i, j, matrix)
            #print cost,
            if min_t == -1 or min_t > cost:
                im, jm = i, j
                min_t = cost
        #print
    print min_t
    print im, jm
