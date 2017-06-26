m,n = raw_input().split()
m = int(m)
n = int(n)
arr = [0]*(n+1)
arr1 = map(int,raw_input().split())
i=0
k=-1
while(i<m):
    arr[arr1[i]]+=1
    age_t = arr[arr1[i]]
    if k==-1 or age_t>arr[k] or arr[k]==age_t and arr1[i]>k:
        k = arr1[i]
    print str(k)+" "+str(arr[k])
    i+=1