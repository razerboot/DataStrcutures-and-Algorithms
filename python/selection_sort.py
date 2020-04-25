
arr = [24,56,12,9,86,23]

#array is divided into sorted and un-sorted
#find min put in sorted and continue the process
def selection_sort(arr):
    s_arr = []
    size = len(arr)
    while(size>len(s_arr)):
        pos = min_arr(arr)
        s_arr.append(arr[pos])
        arr.pop(pos)

    return s_arr

def min_arr(arr):
    a = 100
    b = -1
    for i in range(len(arr)):
        if arr[i]<a:
            a = arr[i]
            b = i
    return b

for i in range(len(arr)):

    min_ind = i
    for j in range(i+1,len(arr)):
        if arr[j]<arr[min_ind]:
            min_ind = j

    arr[i],arr[min_ind] = arr[min_ind],arr[i]

print arr
#print selection_sort(arr)