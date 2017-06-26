def find_pair(arr,x):
    mini = min(arr)
    size = len(arr)
    if mini<0:
        mini = abs(mini)
        for i in range(size):
            arr[i] += mini
        x += 2*mini
    maxi = max(arr)
    m = [0]*(maxi+1)
    for i in range(size):
        if m[arr[i]]==1:
            return arr[i]-mini,(x-arr[i])-mini
        try:
            m[x-arr[i]]=1
        except:
            continue
    return -1e

print find_pair([2,8,11,-4,-2],21)
