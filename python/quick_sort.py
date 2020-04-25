#is a recursive algo for sorting
# quick sort divides the array into two halfes based on partiontion index
def quick_sort(arr,lo,hi):
    if(hi>lo):
        #pi = partition(arr,lo,hi)
        junk = partition_1(arr,lo,hi).split()
        pi_lo = int(junk[0])
        pi_hi = int(junk[1])
        quick_sort(arr,lo,pi_lo-1)
        quick_sort(arr,pi_hi+1,hi)

#partition shuffles the array such that elements less than partition index to one side,
# greater than to other side of partition index
def partition(arr,lo,hi):
    # partition index is choosen as last element always
    k=hi
    j = lo
    for i in range(lo,hi):
        if arr[i]<=arr[k]:
            arr[j],arr[i] = arr[i],arr[j]
            j += 1
    arr[j], arr[k] = arr[k], arr[j]
    k=j-1
    i=j-1
    while i>=lo:
        if arr[i]==arr[j]:
            arr[i],arr[k] = arr[k],arr[i]
            k -= 1
        i -= 1
    #print j
    return str(k+1)+" "+str(j)

def partition_1(arr,lo,hi):
    if(hi-lo==1):
        if arr[lo] < arr[hi]:
            return str(lo+1)+" "+str(hi)
        elif arr[lo]>arr[hi]:
            arr[lo],arr[hi] = arr[hi],arr[lo]
            return str(lo)+" "+str(hi-1)
        elif arr[lo]==arr[hi]:
            return str(lo)+" "+str(hi)
    t = lo
    p = arr[hi]
    while(t<=hi):
        if arr[t]<p:
            arr[lo],arr[t] = arr[t],arr[lo]
            lo += 1
            t += 1
        elif arr[t]>p:
            arr[hi],arr[t] = arr[t],arr[hi]
            hi -= 1
        else:
            t += 1
    return str(lo)+" "+str(hi)

arr = [9,10,9,24,56,23,24,56,12,9,23,27,23,86,23]
quick_sort(arr,0,len(arr)-1)
print arr