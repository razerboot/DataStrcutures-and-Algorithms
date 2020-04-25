
arr = [24,56,12,9,86,23]

#reverse to selection sort
#highest number gets to the end of the array
#from next step array is sorted leaving the last element
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(0,len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]

bubble_sort(arr)
print arr