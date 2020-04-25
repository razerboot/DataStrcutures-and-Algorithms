def pas(n):
    arr = []
    arr.append([1])
    arr.append([1,1])
    i=1
    while(i<n-1):
        arr_temp = []
        for j in range(len(arr[i])):
            if j==0:
                arr_temp.append(arr[i][j])
            else:
                arr_temp.append(arr[i][j]+arr[i][j-1])
        arr_temp.append(arr[i][j])
        arr.append(arr_temp)
        i += 1
    print arr

pas(6)