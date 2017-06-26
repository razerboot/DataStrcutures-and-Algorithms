
# always get right element if there are repetitions
def bs_right(arr,key):
    l=0
    r=len(arr)
    while(r-l>1):
        mid=(r+l)/2
        if arr[mid]<=key:
            l=mid
        else:
            r=mid
    return l,r
#example array
arr=[2,2,2,3,7,9,23,25,25,25,26,27,29,60,60,60,60]

# get the left occurance in case of repetitions
def bs_left(arr,key):
    l=-1
    r=len(arr)
    while(r-l>1):
        mid=(r+l)/2
        if arr[mid]<key:
            l=mid
        else:
            r=mid
    return r,l
print bs_left(arr,60)
print bs_left(arr,29)
print bs_left(arr,25)
print bs_left(arr,2)
