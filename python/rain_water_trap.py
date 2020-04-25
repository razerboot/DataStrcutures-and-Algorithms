arr=[0,1,0,2,1,0,1,3,2,1,2,1]
n=len(arr)
max_left=[0]*(n+1)
max_right=[0]*(n+1)
for i in xrange(n):
	if i==0 or max_left[i-1]<=arr[i]:
		max_left[i]=arr[i]
	else:
		max_left[i]=max_left[i-1]
for i in reversed(xrange(n)):
	if i==n-1 or max_right[i+1]<=arr[i]:
		max_right[i]=arr[i]
	else:
		max_right[i]=max_right[i+1]
trap=0
for i in xrange(n):
	c=min(max_left[i],max_right[i])
	if arr[i]<c:
		trap+=c-arr[i]
print trap

