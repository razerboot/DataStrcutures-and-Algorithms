t = input()

for a0 in xrange(t):
    n, l, a, b = map(int, raw_input().split())
    arr = map(int, raw_input().split())
    arr.sort()
    b = b - n * l
    s_arr = [0] * n
    for i in xrange(n):
        s_arr[i] = arr[i] - i * l
    s_arr.sort()

    if n % 2 == 0:
        x1 = s_arr[n / 2 - 1]
        x2 = s_arr[n / 2]
        if x1 >= b or (x1 > a and x2 > b):
            # if a, b is left to x1, x2
            p = b
        elif x2 <= a or (x1 < a and x2 < b):
            # if a, b is right to x1, x2
            p = a
        elif x1 < a and x2 > b:
            # if a, b is inside x1, x2
            p = a
        elif x1 > a and x2 < b:
            # if a, b covers complete x1, x2 range
            p = x1
    else:
        x1 = s_arr[n / 2]
        if a < x1 < b:
            p = x1
        elif x1 >= b:
            p = b
        else:
            p = a

    val = 0
    for i in xrange(n):
        val += abs(p - s_arr[i])
    print val
