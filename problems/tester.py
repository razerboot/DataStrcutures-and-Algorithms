from random import randrange
arr = [randrange(1, 10 ** 5) for i in xrange(10 ** 5 + 1)]
n = len(arr)
arr1 = set()
for i in xrange(n):
    ele = arr[i]
    if ele > 1:
        while ele <= 10 ** 6:
            arr1.add(ele)
            ele *= arr[i]
print len(arr1)