#!/bin/python

import sys


class Node():
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def insert(curr, key):
    node = Node(key)
    curr.right = node
    node.left = curr
    return node


def delete(prev, curr, nex):
    prev.right = nex
    nex.left = prev
    return nex


g = int(raw_input().strip())
arr=[0]*(100000)
k=0
for i in xrange(100000):
    arr[i]=1-k
    k=1-k
for a0 in xrange(g):
    n = int(raw_input().strip())
    sequence = arr
    if n < 3:
        print "Bob"
        continue
    # if count is odd alice wins, even means bob wins
    root = Node(sequence[0])
    curr = root
    for i in xrange(1, n):
        curr = insert(curr, sequence[i])
    count = 0
    curr = root.right
    while curr.right != None:
        prev = curr.left
        nex = curr.right
        if prev.val == 0 and nex.val == 0:
            curr = delete(prev, curr, nex)
            if prev != root:
                curr = prev
            count += 1
            continue
        while curr.right != None:
            prev = curr.left
            nex = curr.right
            if prev.val == 0 and nex.val == 0:
                break
            curr = curr.right
            # print sequence
    if count == 0 or count % 2 == 0:
        print "Bob"
    else:
        print "Alice"
