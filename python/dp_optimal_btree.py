import sys

def bot_up(k,p,q):
    n=len(k)-1
    c=[[sys.maxint for j in xrange(n+1)] for i in xrange(n+2)]
    root=[[-1 for j in xrange(n+1)] for i in xrange(n+2)]
    w=[[-1 for j in xrange(n+1)] for i in xrange(n+2)]
    for i in xrange(1,n+2):
        c[i][i-1]=q[i-1]
        w[i][i-1]=q[i-1]
    for l in xrange(1,n+1):
        for i in xrange(1,n-l+2):
            j=i+l-1
            w[i][j]=w[i][j-1]+p[j]+q[j]
            for r in xrange(i,j+1):
                t= c[i][r-1]+c[r+1][j]+w[i][j]
                if c[i][j]>t:
                    c[i][j]=t
                    root[i][j]=r
    return c,root



#given probabilities of keys find the tree with minimum expected cost
k=[0,5,11,34,39,45]
d=[3,7,23,36,41,54]
p=[0,.15,.1,.05,.1,.2]
q=[.05,.1,.05,.05,.05,.1]
c,r = bot_up(k,p,q)
print c
print r