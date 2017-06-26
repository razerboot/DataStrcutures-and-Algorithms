def maximalRectangle(A):
    n = len(A)
    m = len(A[0])
    maxi=0
    mat = [[(0, 0, 0) for j in xrange(m)] for i in xrange(n)]
    if A[0][0] == 1:
        mat[0][0] = (1,1, 1)
    for j in xrange(m):
        if A[0][j] == 1:
            mat[0][j] = (mat[0][j - 1][1] + 1,mat[0][j - 1][1] + 1, 1)
    for i in xrange(n):
        if A[i][0] == 1:
            mat[i][0] = (mat[i - 1][0][2] + 1,1, mat[i - 1][0][2] + 1)
    for i in xrange(1, n):
        for j in xrange(1, m):
            al,wl,hl = mat[i][j - 1]
            at,wt,ht = mat[i - 1][j]
            if A[i][j] == 1:
                w_min = min(wl+1,wt)
                h_min = min(hl, ht + 1)
                a1=(wl+1)*h_min
                a2=w_min*(ht+1)
                if a1>a2:
                    mat[i][j] = (a1,wl+1, h_min)
                else:
                    mat[i][j]=(a2,w_min,ht+1)
                if mat[i][j][0] == 0:
                    mat[i][j] = (1, 1, 1)
                if maxi==0 or maxi<mat[i][j][0]:
                    maxi=mat[i][j][0]
    for i in xrange(1, n):
        for j in xrange(1, m):
            al,wl,hl = mat[i][j - 1]
            at,wt,ht = mat[i - 1][j]
            if A[i][j] == 1:
                w_min = min(wl+1,wt)
                h_min = min(hl, ht + 1)
                a1=(wl+1)*h_min
                a2=w_min*(ht+1)
                if a1<a2:
                    mat[i][j] = (a2, w_min, ht + 1)
                else:
                    mat[i][j] = (a1, wl + 1, h_min)
                if mat[i][j][0] == 0:
                    mat[i][j] = (1, 1, 1)
                if maxi==0 or maxi<mat[i][j][0]:
                    maxi=mat[i][j][0]

    print mat
    print maxi


A =[
  [1, 1, 0, 0],
  [0, 0, 0, 0],
  [0, 1, 1, 1],
  [1, 0, 1, 0],
  [1, 1, 1, 1],
  [1, 0, 0, 1]
]
print maximalRectangle(A)