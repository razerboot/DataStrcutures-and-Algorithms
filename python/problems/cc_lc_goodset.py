arr = [1]
nset = set()
p = 2
while len(arr) < 100:
    if p not in nset:
        arr.append(p)
        for a in arr[:-1]:
            nset.add(a + arr[-1])
    p += 1

t = input()
for a0 in xrange(t):
    n = input()
    for i in xrange(n):
        print arr[i],
    print
