
# there are n*len(c) states or subproblems, at each state we have 2 subproblems so time complexity O(n*len(c))
def dp_coin_change(n,c):
    m=len(c)
    count=[[0 for j in xrange(m+1)] for i in xrange(n+1)]
    #creating count 0 base case
    for j in xrange(m+1):
        count[0][j]=1
    #no coins but there is count
    for i in xrange(1,n+1):
        count[i][0]=0

    for i in xrange(1,n+1):
        for j in xrange(1,m+1):
            #atleast one jth coin 1based indexing
            if i-c[j-1]>=0:
                c1 = count[i-c[j-1]][j]
            else:
                c1=0
            #no jth coin 1based indexing
            c2=count[i][j-1]
            count[i][j]=c1+c2
    return count
n=10
c=[2,5,3,6]
print dp_coin_change(n,c)