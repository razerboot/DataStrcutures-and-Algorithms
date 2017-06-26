def dp(s,k):
    m=len(s)
    mat=[[False for j in xrange(m+1)] for i in xrange(k+1)]
    for j in xrange(m):
        mat[0][j]=True
    for i in xrange(1,k+1):
        for j in xrange(1,m+1):
            if i-s[j-1]>=0:
                mat[i][j]= mat[i-s[j-1]][j-1] or mat[i][j-1]
            else:
                mat[i][j]=mat[i][j-1]
    print mat



s=[3,1,1,2,2,1]
#partition into two subsets of equal sum
#given all numbers are positive
# np-complete problem
# but for smaller sums can be solved in O(sum*len(s))
k=sum(s)
if k%2==0:
    k/=2
    dp(s,k)
else:
    print "nope"
