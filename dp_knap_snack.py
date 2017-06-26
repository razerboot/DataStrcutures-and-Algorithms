#lower state is defined as either considering a element in arr or not
def dp_knap_snack(val,w,W):
    m=len(w)
    mat=[[0 for j in xrange(m)] for i in xrange(W+1)]
    #base case where W=0 and there are weights to consider arr values will be 0

    # for W>0 and only first weight to consider
    for i in xrange(1,W+1):
        if i-w[0]>=0:
            mat[i][0]=val[0]
    for i in xrange(1,W+1):
        for j in xrange(1,m):
            #case1 if jth weight is considered #assumed 1based indexing in matrix
            c1=0
            if i-w[j]>=0:
                c1=mat[i-w[j]][j-1]+val[j]
            #case2 if jth weight not considered
            c2=mat[i][j-1]
            mat[i][j]=max(c2,c1)
    return mat[W][m-1]

val=[60,100,120]
w=[10,20,30]
W=50
print dp_knap_snack(val,w,W)