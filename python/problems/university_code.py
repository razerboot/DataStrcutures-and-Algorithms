#!/bin/python

import sys

def try(s,n,sp):
    i=0
    while(i+2*sp+1<=n):
        if s[i:i+sp]+1==s[i+sp:i+2*sp]:
            i+=1
        elif s[i:i+sp]+1==s[i+sp:i+2*sp+1]:
            i+=1
def check_b(s,n):
    if n==1:
        return "NO"
    elif n=2:
        if s[0]+1==s[1]:
            return "YES",s[0]
        else:
            return "NO"
    split=n/2
    sp=1
    while(s<=split):
        temp = try(s,n,sp)
        if temp[0]=="YES":
            return  temp
        sp+=1
    return "NO"
q = int(raw_input().strip())
for a0 in xrange(q):
    s = raw_input().strip()
    print check_b(s,len(s))
    # your code goes here
