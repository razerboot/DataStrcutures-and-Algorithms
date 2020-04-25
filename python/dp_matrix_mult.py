import sys
# p0 and p1 correspond to matrix 1, there are 6 matrices
p=[5,10,3,12,5,50,6]
size= len(p)-1
# storing split k of an i,j segment
s=[[-1 for j in xrange(size+1)] for i in xrange(size+1)]
#storing the cost or scalar mult need for i,j segment
m=[[sys.maxint for j in xrange(size+1)] for i in xrange(size+1)]

for i in xrange(1,size+1):
    m[i][i]=0
#optimal parenthesization

# 1. bottom up approach
def bot_up(p,m,s,n):
    for l in xrange(2,n+1):
        for i in xrange(1,n-l+2):
            j=i+l-1
            for k in xrange(i,j):
                q=m[i][k]+m[k+1][j]+(p[i-1]*p[k]*p[j])
                if m[i][j]>q:
                    m[i][j]= q
                    s[i][j]=k
def sol(s,i,j):
    if i==j:
        return str(i)
    return "("+sol(s,i,s[i][j])+sol(s,s[i][j]+1,j)+")"
bot_up(p,m,s,size)
print sol(s,2,size-1)







