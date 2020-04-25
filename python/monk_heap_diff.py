import heapq as pq
from math import ceil

def f(x):
    return -1*int(x)
n,k=map(int,raw_input().split())
arr = map(f,raw_input().split())
sum_old=0
for ele in arr:
    sum_old+=(ele*-1)

pq.heapify(arr)
#print arr
while(k>0):
    temp=[]
    while(arr!=[] and arr[0]==-1):
        temp.append(pq.heappop(arr))
    if arr!=[]:
        v = ceil((arr[0]*-1)/3.0)
        pq.heapreplace(arr,(v*-1))
    for ele in temp:
        arr.append(ele)
    pq.heapify(arr)
    k-=1
#print arr
sum_new=0
for ele in arr:
    sum_new+=(ele*-1)

print '{0:.6f}'.format(sum_old/n),
print '{0:.6f}'.format(sum_new/n)