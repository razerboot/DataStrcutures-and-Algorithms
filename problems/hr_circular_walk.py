#!/bin/python

from random import randrange
from timeit import default_timer as timer


def find_distance(s, ele, n):
    k = (ele - s + n) % n
    return min(k, n - k)


def find_boundaries(type, ele, dist, left, right, s, d, r, n, dis, mini1_left, mini1_val, maxi1_right, maxi1_val):

    if type == 'maxi':
        for i in xrange(dist + right + 1, r[ele] + 1):

            c = (ele + i + n) % n
            if dis[c] == -1:
                if c == d:
                    return True, dis[ele] + 1
                dis[c] = dis[ele] + 1
                dist1 = find_distance(s, c, n)
                k = dist1 - r[c]
                if k < mini1_left:
                    mini1_val = c
                    mini1_left = k
                k = r[c] + dist1
                if k > maxi1_right:
                    maxi1_val = c
                    maxi1_right = k

    if type == 'mini':
        for i in xrange(-1 * r[ele], left + dist):

            c = (ele + i + n) % n
            if dis[c] == -1:
                if c == d:
                    return True, dis[ele] + 1
                dis[c] = dis[ele] + 1
                dist1 = find_distance(s, c, n)
                k = -1 * (dist1 + r[c])
                if k < mini1_left:
                    mini1_val = c
                    mini1_left = k
                k = r[c] - dist1
                if k > maxi1_right:
                    maxi1_val = c
                    maxi1_right = k

    return mini1_left, mini1_val, maxi1_right, maxi1_val


def bfs(r, s, n, d):
    dis = [-1] * n
    dis[s] = 0
    left = 0
    right = 0
    mini_left = -1 * r[s]
    mini_val = s
    maxi_right = r[s]
    maxi_val = s
    mini1_left, maxi1_right = mini_left, maxi_right
    mini1_val, maxi1_val = None, None

    while mini_val is not None or maxi_val is not None:
        if mini_val is not None:
            ele = mini_val
            distance = find_distance(s, ele, n)
            c1 = find_boundaries('mini', ele, distance, left, right, s, d, r, n, dis, mini1_left, mini1_val, maxi1_right, maxi1_val)
            if c1[0] is True:
                return c1[1]
            mini1_left, mini1_val, maxi1_right, maxi1_val = c1

        if maxi_val is not None:
            ele = maxi_val
            distance = -1 * find_distance(s, ele, n)
            c1 = find_boundaries('maxi', ele, distance, left, right, s, d, r, n, dis, mini1_left, mini1_val, maxi1_right, maxi1_val)
            if c1[0] is True:
                return c1[1]
            mini1_left, mini1_val, maxi1_right, maxi1_val = c1

        left, right = mini_left, maxi_right
        mini_left, maxi_right = mini1_left, maxi1_right
        mini_val, maxi_val = mini1_val, maxi1_val
        mini1_val, maxi1_val = None, None

    return dis[d]


def main_function():
    #n, s, d = map(int, raw_input().split())
    n = 10 ** 7
    r = [0] * n
    #r[0], g, seed, mod = map(int, raw_input().split())

    s = randrange(1, n)
    d = randrange(1, n)
    mod = randrange(1, 10 ** 2)
    r[0] = randrange(1, mod - 1)
    g = randrange(1, mod - 1)
    seed = randrange(1, mod - 1)

    for i in xrange(1, n):
        r[i] = ((r[i - 1] * g) % mod + seed % mod) % mod

    if s == d:
        print 0
    else:
        dis = bfs(r, s, n, d)
        print dis


start = timer()
main_function()
end = timer()
print end - start
