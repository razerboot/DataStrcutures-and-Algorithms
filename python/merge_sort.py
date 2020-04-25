

#divides array in 2 halfes and do this till only one element left then run merge
#1.merge like insertion sort
#2.select lowest of first two and do this till all are inserted

#k=0

def merge_sort(arr,l,r,k):
    if r-l>0:
        size = l+r
        mid = (size-(size%2))/2
        merge_sort(arr, l, mid, k)
        merge_sort(arr, mid + 1, r, k)
        merge_real(arr, l, mid, r)
        #k += merge_sort(arr,l,mid,k)+merge_sort(arr,mid+1,r,k)+merge(arr,l,mid,r)
        #return k
        #k += merge(arr,l,mid,r)
    else:
        return 0
    #return k

# merge using insertion sort locally
def merge(arr,l,mid,r):
    #k = 0
    for i in range(mid+1,r+1):
        j = i-1
        while(j>=l and arr[j]>arr[j+1]):
            arr[j],arr[j+1] = arr[j+1],arr[j]
            #k = k+1
            j = j-1
    #return k

# merge sequentially
def merge_real(arr,l,mid,r):
    l1 = mid-l+1
    l2 = r-mid
    arr1 = [0]*l1
    arr2 = [0]*l2
    for i in range(l1):
        arr1[i] = arr[l+i]

    for i in range(l2):
        arr2[i] = arr[mid+1+i]

    a1 = 0
    a2 = 0
    k = l
    while(a1<l1 and a2<l2):
        if arr1[a1]>arr2[a2]:
            arr[k] = arr2[a2]
            a2 += 1
        else:
            arr[k] = arr1[a1]
            a1 += 1
        k += 1

    if l1-a1>=1:
        for i in range(a1,l1):
            arr[k] = arr1[i]
            k +=1
    if l2-a2>=1:
        for i in range(a2,l2):
            arr[k] = arr2[i]
            k += 1



arr = [24,56,12,9,86,23]

#print merge(arr,0,0,1)
#print merge(arr,0,1,2)
#print merge(arr,3,3,4)
#print merge(arr,3,4,5)
#print merge(arr,0,2,5)
merge_sort(arr,0,len(arr)-1,0)
print arr
#print k