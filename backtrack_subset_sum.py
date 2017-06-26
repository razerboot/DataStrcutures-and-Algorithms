def print_sum(arr,k):
    arr2 = []
    arr1 = []
    arr.sort()
    find_subset(arr1,arr,0,k,len(arr))
    #print arr2



def find_subset(arr1,arr,p,k,N):
    #if k<0:
    #    return
    if k==0:
        print arr1
        return True
    for i in range(p,N):
        if arr[i]<=k:
            arr1.append(arr[i])
            if find_subset(arr1,arr,i+1,k-arr[i],N):
                arr1.pop()
                break
            arr1.pop()
    return

print_sum([4,3,2,1,7,3,5,8,9],10)
