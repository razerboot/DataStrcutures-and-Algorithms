import math

def max_heapify(arr,i,N):
    largest = i
    left = 2*i
    right = 2*i+1

    if left<=N and arr[left]>arr[largest]:
        largest = left
    if right<=N and arr[right]>arr[largest]:
        largest=right

    if i!=largest:
        arr[i],arr[largest]=arr[largest],arr[i]
        max_heapify(arr,largest,N)

def get_height(arr):
    N = len(arr)-1
    return math.ceil(math.log(N+1,2))

def build_maxheap(arr,N):
    i = N/2
    while(i>0):
        max_heapify(arr,i,N)
        i -=1

def insert_to_heap(arr,key,N):
    arr.append(key)
    N += 1
    i = N
    p = N/2
    while(p>=1 and arr[i]>arr[p]):
        arr[i],arr[p]=arr[p],arr[i]
        i /= 2
        p /= 2


def extract_max(arr):
    N = len(arr)-1
    #use heapify
    arr[1],arr[N] = arr[N],arr[1]
    value = arr.pop()
    max_heapify(arr,1,N-1)
    return value

def find_max():
    return arr[1]


def heap_sort(arr,N):
    build_maxheap(arr,N)
    i=N
    while(i>1):
        arr[1],arr[i]=arr[i],arr[1]
        max_heapify(arr,1,i-1)
        i -= 1
    #use build_maxheap once
    #use heapify


arr =[0]
n = int(raw_input())
arr1= map(int,raw_input().strip().split())
arr.extend(arr1)
print get_height(arr)
build_maxheap(arr,n)
print arr
print get_height(arr)
print extract_max(arr)
print arr
print get_height(arr)
print extract_max(arr)
print arr
print get_height(arr)

insert_to_heap(arr,200,len(arr)-1)
print arr
