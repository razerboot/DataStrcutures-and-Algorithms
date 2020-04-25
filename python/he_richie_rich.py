#!/bin/python

import sys

n, k = raw_input().strip().split(' ')
n, k = [int(n), int(k)]
number = list(raw_input().strip())
vi = [0] * (n)
i = 0
j = n - 1
while (i < j):
    if number[i] != number[j]:
        k -= 1
        if k < 0:
            print -1
            break
        if number[i] > number[j]:
            vi[j] = 1
            number[j] = number[i]
        else:
            vi[i] = 1
            number[i] = number[j]
    print i,j
    i += 1
    j -= 1
else:
    if k > 0:
        i = 0
        j = n - 1
        while (i < j):
            if number[i] != 9 and (vi[i] == 1 or vi[j] == 1):
                if k < 1:
                    break
                k -= 1
                number[i] = 9
                number[j] = 9
            elif number[i]!=9 and vi[i]==0 and vi[j]==0:
                if k >= 2:
                    k -= 2
                    number[i] = 9
                    number[j] = 9
            print i,j
            i += 1
            j -= 1
        if k > 0 and n % 2 != 0:
            number[(n - 1) / 2] = 9
    print ''.join(map(str, number))

