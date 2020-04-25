def count_sort(arr):
    a = arr[min(arr)]
    b = arr[max(arr)]
    arr1 = {}
    # creating a count array
    for i in range(a,b):
        if arr[i]<=b and arr[i]>=a:
            if arr[i] in arr1:
                arr1[str(i)] += 1
            else:
                arr1[str(i)] = 1
    return arr1
#modifying count array
def adding(arr,i):
    if i==0:
        return arr[0]
    arr[i] = arr[i]+adding(arr,i-1)
    return arr

for i in range(arr):
    index = arr1[str(arr[i])]
    if i!=index:
        arr1




