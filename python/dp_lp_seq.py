s="abddbaccda"
n=len(s)
mat=[[0 for j in xrange(n)] for i in xrange(n)]
for i in xrange(n):
    mat[i][i]=1
for l in xrange(2,n+1):
    for i in xrange(0,n-l+1):
        j=i+l-1
        if s[i]==s[j]:
            mat[i][j]=mat[i+1][j-1]+2
        else:
            mat[i][j]=max(mat[i+1][j],mat[i][j-1])
#print mat

# technique using lcs
#since reverse of palindrome is a palindorme we can do this
sr=s[::-1]
mat=[[0 for j in xrange(n)] for i in xrange(n)]
