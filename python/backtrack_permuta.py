def permutations(str1):
    arr2 = []
    arr1 = []
    arr = {}
    for ele in str1:
        if ele in arr:
            arr[ele] += 1
        else:
            arr[ele] = 1
    find_all(arr2,arr1,arr,len(str1))
    return arr2,len(arr2)

def create_list(a1):
    return ''.join(a1)
def find_all(arr2,arr1,arr,c):
    if c==0:
        arr2.append(create_list(arr1))
        return
    for ele in arr:
        if(arr[ele]>0):
            arr1.append(ele)
            arr[ele] -= 1
            find_all(arr2,arr1,arr,c-1)
            arr[ele] += 1
            arr1.pop()
    return

print permutations("ABCC")