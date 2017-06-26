arr= [10, 22, 9, 33, 21, 50, 41, 60, 80]

#optimal solution of problem is within optimal solutions to subproblems
# overlapping because both problem and subproblem depend on another subproblem
# so dp with i choices at ith subproblem, n overall subproblems so time complexity of n^2
l = len(arr)
c=[0]*l
c[0]=1
maxi=0
for i in xrange(1,l):
    c[i]=1
    for j in xrange(0,i):
        if arr[i]>arr[j]:
            c[i] = max(c[j]+1, c[i])
    maxi=max(maxi,c[i])
print maxi