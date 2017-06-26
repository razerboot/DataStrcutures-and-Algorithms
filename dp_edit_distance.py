#edit distance
# time complexity O(n^2)
# constant number of choices 1 or 3 at each subproblem, n^2 subproblems for i in str1 and j in str2
def dp_edit(inp,out):
    n=len(inp)
    m=len(out)
    mat=[[0 for j in xrange(m+1)] for i in xrange(n+1)]
    # insertions
    for j in xrange(1,m+1):
        mat[0][j]=j
    #deletions
    for i in xrange(n+1):
        mat[i][0]=i
    for i in xrange(1,n+1):
        for j in xrange(1,m+1):
            if inp[i-1]==out[j-1]:
                mat[i][j]=mat[i-1][j-1]
            # 1 signifies insertion(i,j-1) or deletion(i-1,j) or replace(i-1,j-1)
            # mat[i][j] value says no of operations to change from i to j
            else:
                mat[i][j]=min(mat[i-1][j],mat[i][j-1],mat[i-1][j-1])+1

    return mat[n][m]

inp="sunday"
out="saturday"
print dp_edit(inp,out)