# finding kth smallest element in row wise and column wise sorted matrix

# complexity of k*(m+n) where m is row length and n is column length
def adjust(matrix,x,y):
    n=len(matrix)
    m=len(matrix[x])
    while(x<n and y<m):
        minx,miny = x,y
        leftx,lefty=x+1,y
        rightx,righty=x,y+1
        if leftx<n and lefty<len(matrix[leftx])  and matrix[leftx][lefty]<matrix[minx][miny]:
            minx,miny=leftx,lefty
        if righty<len(matrix[x]) and rightx<n and matrix[rightx][righty]<matrix[minx][miny]:
            minx,miny = rightx,righty
        if (minx,miny) == (x,y):
            break
        else:
            matrix[x][y],matrix[minx][miny]=matrix[minx][miny],matrix[x][y]
            x,y = minx,miny

def matrix_pop(matrix):
    n=len(matrix)
    m=len(matrix[n-1])
    if n==1 and m==1:
        return matrix[0].pop()
    while matrix[n-1]==[]:
        matrix.pop()
        n=len(matrix)
    last = matrix[n-1].pop()
    first=matrix[0][0]
    matrix[0][0]=last
    adjust(matrix,0,0)
    return first


def k_matrix_pop(matrix,k):
    for i in xrange(k-1):
        matrix_pop(matrix)
    return matrix_pop(matrix)

matrix=[]
n,m = map(int,raw_input().split())
for a0 in xrange(n):
    row=list(map(int,raw_input().split()))
    matrix.append(row)
print k_matrix_pop(matrix,25)
print matrix
'''
# input
5 5
1 3 5 7 9
6 8 11 13 15
10 21 25 27 29
12 22 26 29 30
13 23 31 34 37
'''