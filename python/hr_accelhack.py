from timeit import timeit as ti
from collections import Counter
def seive(n):
    i=2
    num=[0]*(n+1)
    p=[]
    while(i*i<=n):
        j=i
        while(j*i<=n):
            num[i*j]=1
            j+=1
        i+=1
    for i in xrange(2,n+1):
        if num[i]==0:
            p.append(i)
    return p

def factorize(n):
    sq=int(n**0.5)
    p=seive(sq)
    c=Counter()
    for prime in p:
        while(n%prime==0):
            n /= prime
            c[prime]+=1
    return c
#print factorize(10000)
print ti("factorize(1213231313131)",setup="from __main__ import factorize",number=1)


