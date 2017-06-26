#!/bin/python

import sys

def dp(n, m, b, sum_array, matrix):
    mod = 10 ** 9 + 7
    for i in xrange(2, n + 1):
        for j in xrange(m):
            matrix[i][j] = sum_array[i - 1]
            if i > b[j]:
                # term 1 - number of ways for length i-1
                # term 2 - number of ways for length i-b[j]-1
                # term 3 - number of ways for length i-b[j]-1 with j'type as last element
                # term 2 - term 3 is number of ways b[j] to i - 1 has all elements with j'type as element
                # also same as where i - b[j] - 1 element is not j'type as last element
                matrix[i][j] = matrix[i][j] - (sum_array[i - b[j] - 1] - matrix[i - b[j] - 1][j])
            sum_array[i] = (sum_array[i] + matrix[i][j]) % mod

    return sum_array[n]

s = input()
mod = 10 ** 9 + 7
for a0 in xrange(s):
    n, m = map(int, raw_input().split())
    b = map(int, raw_input().split())
    sum_array = [0] * (n + 1)
    matrix = [[0 for j in xrange(m)] for i in xrange(n + 1)]
    for j in xrange(m):
        matrix[1][j] = 1
    sum_array[1] = m
    sum_array[0] = 1

    print dp(n, m, b, sum_array, matrix)
    # print matrix
    # print sum_array
