import sys
from collections import defaultdict
import operator

n, c = raw_input().strip().split(' ')
n, c = [int(n), int(c)]
crate = []
for crate_i in xrange(c):
    crate_temp = map(int, raw_input().strip().split(' '))
    crate.append(crate_temp)
#print crate
d = defaultdict(int)
for k,v in crate:
    d[v] += k

d1 = sorted(d.items(),key=operator.itemgetter(0),reverse=True)
i = 0
n1 = 0
matches = 0
while (n1 < n):
    matches += d1[i][0]*d1[i][1]
    n1 += d1[i][1]
    i += 1
if n1 == n:
    print matches
else:
    while (n1 > n):
        matches -= d1[i - 1][0]
        n1 -= 1
    print matches