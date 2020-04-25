
p=[0,1,5,8,9,10,17,17,20,24,30]
n=10
r=[-1]*(n+1)
r[0]=0
s=[-1]*(n+1)
# solving recursively with memoization

def top_down_dp(p,r,n):
    if r[n]>=0:
        return r[n]
    m=-1
    for i in xrange(1,n+1):
        m=max(m,p[i]+top_down_dp(p,r,n-i))
    return m

#building solution for lower states and proceding to top

def bot_up_dp(p,r,n,c):
    for j in xrange(1,n+1):
        m=-1
        for i in range(1,j+1):
            if i==j:
                m=max(m,p[i]+r[j-i])
            else:
                m=max(m,p[i]+r[j-i]-c)
        r[j]=m
    return r




print top_down_dp(p,r,n)
r=[-1]*(n+1)
r[0]=0
c=1
print bot_up_dp(p,r,n,c)
c=0
print bot_up_dp(p,r,n,c)