#heap is a complete binary tree
# for index i(1 based) childs are at 2*i and 2*i+1
#building min heap

#function heapify to convert any normal array to min heap
def heapify(heap,n):
    for i in reversed(xrange(1,n+1)):
        adjust(heap,i,n)


# function adjust used by heap pop, heapify and replace functions to change heap invalid to valid stage
def adjust(heap,p,n):
    while(p<=n):
        left=2*p
        right=2*p+1
        mini=p
        if left<=n and heap[left]<heap[mini]:
            mini=left
        if right<=n and heap[right]<heap[mini]:
            mini=right
        if mini==p:
            break
        else:
            heap[p],heap[mini]=heap[mini],heap[p]
            p=mini


def heap_pop(heap):
    n=len(heap)-1
    if n==0:
        return
    last=heap.pop()
    first=heap[1]
    heap[1]=last
    adjust(heap,1,n-1)
    return first
n=input()
arr=[0]+list(map(int,raw_input().split()))
heapify(arr,n)
print arr
print heap_pop(arr)
print arr

