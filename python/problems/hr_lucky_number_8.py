mod = 10 ** 9 + 7


def count1(ele, num):
    ele = str(ele)
    n = len(ele)
    arr = [0] * n
    for ch in num:
        for i in reversed(xrange(n)):
            if ch == ele[i]:
                if i == 0:
                    arr[i] += 1
                else:
                    arr[i] += arr[i - 1]
    return arr[-1]


def count2(ele, num, n, powers):
    ele = str(ele)[::-1]
    m = len(ele)
    arr = [0] * m
    c = 0
    for i in reversed(xrange(n)):
        for j in reversed(xrange(m)):
            if ele[j] == num[i]:
                if j == 0:
                    arr[j] += 1
                elif j == m - 1:
                    if arr[j - 1] != 0:
                        c = (c + (arr[j - 1] * powers[i]) % mod) % mod
                else:
                    arr[j] += arr[j - 1]
    return c
n = input()
powers = [1] * (n + 1)
for i in xrange(n + 1):
    powers[i] = (2 * powers[i - 1]) % mod
num = raw_input()
c = 0
div_8 = [8 * i for i in xrange(125)]
#print div_8
for i in xrange(1, 12):
    #c_old = c
    c = (c + count1(div_8[i], num)) % mod
    #if c_old != c:
    #    print div_8[i], c
for i in xrange(12, 125):
    #c_old = c
    c = (c + count2(div_8[i], num, n, powers)) % mod
    #if c_old != c:
    #    print div_8[i], c
print c