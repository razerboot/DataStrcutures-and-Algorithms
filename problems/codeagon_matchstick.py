#!/bin/python

import sys

n, c = raw_input().strip().split(' ')
n, c = [int(n), int(c)]
crate = []
for crate_i in xrange(c):
    crate_temp = map(int, raw_input().strip().split(' '))
    crate.append(crate_temp)


# your code goes here
def max_matches(crate):
    if n == 0:
        return 0
    maxi = 0
    for i in range(c):
        maxi += crate[i][0]
    if n >= maxi:
        matches = 0
        for i in range(c):
            matches += crate[i][0] * crate[i][1]
        return matches
    crate1 = {}
    crate2 = []
    for i in range(c):
        crate1[crate[i][1]] = crate[i][0]
        crate2.append(crate[i][1])

    crate2.sort(reverse=True)
    # print crate2
    # print crate1
    i = 0
    n1 = 0
    matches = 0
    while (n1 < n):
        matches += crate2[i] * crate1[crate2[i]]
        n1 += crate1[crate2[i]]
        i += 1
    if n1 == n:
        return matches
    else:
        while (n1 > n):
            matches -= crate2[i - 1]
            n1 -= 1
        return matches


print max_matches(crate)
