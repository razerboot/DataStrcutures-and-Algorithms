k1="314159265358979323846264338327953141592653589793238462643383279531415926535897932384626433832795314159265358979323846264338327953141592653589793238462643383279531415926535897932384626433832795314159265358979323846264338327953141592653589793238462643383279531415926535897932384626433832795"

k2="314159265358979323846264338327953141592653589793238462643383279531415926535897932384626433832795314159265358979323846264338327953141592653589793238462643383279531415926535897932384626433832795314159265358979323846264338327953141592653589793238462643383279531415927535897932384626433832795"
import hashlib
from collections import Counter
arr=[]

k=10**6
while(k>0):
    if k%2==0:
        arr.append(k1)
    else:
        arr.append(k2)
    k-=1

#!/bin/python

import sys
def compare(x,y):
    x=x[0]
    y=y[0]
    if len(x)>len(y):
        return 1
    elif len(x)<len(y):
        return -1
    elif hashlib.md5(x).digest()==hashlib.md5(y).digest():
        return 0
    else:
        for i in xrange(len(x)):
            if x[i]<y[i]:
                return -1
            elif x[i]>y[i]:
                return 1


#temp = arr.items()
#temp.sort(cmp=compare)
#for ele in temp:
#    n=ele[0]
#    c=ele[1]
#    while(c>0):
#        print n
#        c-=1
# your code goes here
arr.sort(cmp=compare)
print len(k1)
#for ele in arr:
#    print ele