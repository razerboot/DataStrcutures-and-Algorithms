#!/bin/python

import sys, random
from collections import deque


def find_distance(s, ele, n):
    k = (ele - s + n) % n
    return min(k, n - k)


def bfs(r, s, n, d):
    dis = [-1] * n
    dis[s] = 0
    left = -1 * r[s]
    right = r[s]
    q_left = deque([])
    q_right = deque([])
    for i in xrange(-1 * r[s], 0):
        ele = (s + i + n) % n
        dis[ele] = 1
        q_left.append(ele)
    for i in xrange(1, r[s] + 1):
        ele = (s + i + n) % n
        dis[ele] = 1
        q_right.append(ele)
    # print q_left
    # print q_right
    q1_left = deque([])
    q1_right = deque([])
    while len(q_left) > 0 or len(q_right) > 0:

        for ele in q_left:
            # looking through nodes left to source s
            distance = find_distance(s, ele, n)
            # print ele, s, distance + right + 1, r[ele] + 1
            # for every node left to s we are finding nodes from right to right end
            for i in xrange(distance + right + 1, r[ele] + 1):
                c = (ele + i + n) % n
                if dis[c] == -1:
                    if c == d:
                        return dis[ele] + 1
                    dis[c] = dis[ele] + 1
                    q1_right.append(c)

            right = max(r[ele] - distance, right)
            # for every node left to s we are finding from left to left end
            for i in xrange(-1 * r[ele], left + distance):
                c = (ele + i + n) % n
                if dis[c] == -1:
                    if c == d:
                        return dis[ele] + 1
                    dis[c] = dis[ele] + 1
                    q1_left.append(c)

            left = min(left, -1 * (distance + r[ele]))

        for ele in q_right:
            distance = find_distance(s, ele, n)
            for i in xrange(right + 1 - distance, r[ele] + 1):
                c = (ele + i + n) % n
                if dis[c] == -1:
                    if c == d:
                        return dis[ele] + 1
                    dis[c] = dis[ele] + 1
                    q1_right.append(c)

            right = max(r[ele] + distance, right)
            for i in xrange(-1 * r[ele], left - distance):
                c = (ele + i + n) % n
                if dis[c] == -1:
                    if c == d:
                        return dis[ele] + 1
                    dis[c] = dis[ele] + 1
                    q1_left.append(c)

            left = min(left, -1 * (r[ele] - distance))
        # print q1_left
        # print q1_right
        q_left, q1_left = q1_left, q_left
        q_right, q1_right = q1_right, q_right
        q1_left.clear()
        q1_right.clear()

    return dis[d]

n, s, d = map(int, raw_input().split())
#n = 10 ** 7
#s = random.randrange(1, n)
#d = random.randrange(1, n)
r = [0] * n
#p = random.randrange(1, 10 ** 2)
r[0], g, seed, mod = map(int, raw_input().split())
#r[0] = random.randrange(1, p - 1)
#g = random.randrange(1, p - 1)
#seed = random.randrange(1, p - 1)
#mod = p

for i in xrange(1, n):
    r[i] = ((r[i - 1] * g) % mod + seed % mod) % mod

if s == d:
    print 0
else:
    dis = bfs(r, s, n, d)

print dis
