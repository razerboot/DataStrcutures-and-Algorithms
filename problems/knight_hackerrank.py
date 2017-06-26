#!/bin/python

import sys
from collections import deque

n = input()
# your code goes here
arr = [[-1 for j in xrange(n)] for i in xrange(n)]
b = [[0 for j in xrange(n)] for i in xrange(n)]
s={}
s = set()
stack=deque()

def check_pos(i, j, end):
    if 0 <= i <= end and 0 <= j <= end:
        return True
    else:
        return False


def find_path(i,j,arr,moves,end,s,b):
    mini=0
    for x in xrange(0,end+1):
        for y in xrange(0,end+1):
            if x==0 and y==0:
                b[i][j]=0
            else:
                for ele in moves:
                    new_i=ele[0]
                    new_j=ele[1]
                    if check_pos(new_i,new_j,end):
                        if new_i==0 and new_j==0:
                            arr[i][j]=1
                        elif b[]

    if (0,0) in s:
        arr[i][j]=k
    else:
        arr[i][j]=-1
    stack.clear()
    set={}


# print arr
# print b
i = 1
end = n - 1
mid = end / 2
while (i < n):
    j = 1
    while (j < n):
        if arr[j][i] != -1:
            arr[i][j] = arr[j][i]
        elif i == j:
            if end % i == 0:
                arr[i][j] = end / i
            else:
                arr[i][j] = -1
        elif i == 1 and j == n - 2:
            arr[i][j] = 2
        elif i == 1 and j == n - 1:
            if n % 2 == 0:
                arr[i][j] = n - 1
            else:
                arr[i][j] = 2 * (n - 1)
        elif i > mid and j > mid:
            arr[i][j] = -1
        elif i == end and j == end:
            arr[i][j] = 1
        else:
            n_i = -1 * i
            n_j = -1 * j
            moves = [(n_i, n_j), (n_j, n_i), (n_i, j), (i, n_j), (n_j, i), (j, n_i)]
            find_path(i, j,arr, end, end,moves, end,s,b)
        print arr[i][j],
        j += 1
    print ""
    i += 1
# print arr

