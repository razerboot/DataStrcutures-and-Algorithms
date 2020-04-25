def ls(arr):
    max_current = -1
    max_so_far = -1
    for i in range(len(arr)):
        max_current += arr[i]
        if max_current<0:
            max_current = 0
        if max_so_far<max_current:
            print i
            max_so_far = max_current

    return max_so_far

print ls([-2,-3,4,-1,-2,1,5,-3])