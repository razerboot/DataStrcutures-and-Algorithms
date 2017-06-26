arr=[0 , 8 , 4, 12, 2, 10 , 6 , 14 , 1 , 9 , 5 , 13, 3, 11 , 7 , 15]
n=len(arr)
q=[[0 for j in xrange(3)] for i in xrange(n)]
q[0]=[1,0,1]
if arr[1] > arr[0]:
    q[1] = [2, 0, 1]
else:
    q[1] = [1, 0, 2]
maxi=2
for i in xrange(2,n):
    for j in xrange(i):
        if arr[i]>arr[j]:
            q[i][0]=max(q[i][0],q[j][0]+1)
            q[i][1] = max(q[i][1], q[j][1] + 1)
        if arr[i]<arr[j]:
            q[i][1]=max(q[i][1],q[j][1]+1)
            q[i][2]=max(q[i][2],q[j][2]+1)
    if maxi<max(q[i]):
        maxi=max(q[i])
print q
