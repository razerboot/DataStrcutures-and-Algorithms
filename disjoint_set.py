
n,m=map(int,raw_input().split())

arr=[i for i in xrange(n+1)]
size={}
for ele in arr:
	if ele!=0:
		size[ele]=1


#finding root by path compression
def root(arr,v):
	while(v!=arr[v]):
		temp=arr[arr[v]]
		v=temp
	return v


#union using root
def union(arr,size,x,y):
	root_x=root(arr,x)
	root_y=root(arr,y)
	if root_x!=root_y:
# checking size of each tree to make final tree balanced
		if size[root_x]>size[root_y]:
			arr[root_y]=root_x
			size[root_x]+=size[root_y]
			del size[root_y]
		else:
			arr[root_x]=root_y
			size[root_y]+=size[root_x]
			del size[root_x]



while(m>0):
    x,y = map(int,raw_input().split())
    union(arr,size,x,y)
    values = sorted(size.values())
    print " ".join(map(str,values))
    m -= 1
