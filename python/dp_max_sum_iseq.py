arr= [10, 22, 9, 33, 21, 50, 41, 60, 80]
n=len(arr)
q=[0]*n
q[0]=10
maxi=0
for l in xrange(1,n):
    for i in xrange(l):
        if arr[l]>arr[i]:
            q[l]=max(q[l],q[i]+arr[l])
    if q[l]>maxi:
        maxi=q[l]
print q