#sorts like we sort the playing cards in our hands
#two parts of array 1. locally sorted and not sorted
# take each element of unsorted array and move it to left till it finds a number greater than it
def inser_sort(arr):
    size = len(arr)
    for i in range(1,size):
        j =  i-1
        while(arr[j]>arr[j+1]):
            arr[j],arr[j+1] = arr[j+1],arr[j]
            if j ==0:
                break
            j = j-1

    return arr
arr = [24,56,12,9,86,23]
print inser_sort(arr)