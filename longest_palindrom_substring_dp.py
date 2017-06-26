def lps_dp(str):
    size = len(str)
    x,y = size,size
    l = [[-1 for i in range(x)] for y in range(y)]
    i = 0
    while(i<size):
        l[i][i] = "true"
        i +=1
    for y in range(size):
        for x in range(y+1):
            if l[y][x] == -1:
                if x+1==y:
                    if str[x] == str[y]:
                        l[y][x] = "true"
                    else:
                        l[y][x] = "false"
                else:
                    if str[x] == str[y] and l[y-1][x+1] == "true":
                        l[y][x] = "true"
                    else:
                        l[y][x] = "false"
    max = 0
    for y in range(size):
        for x in range(y+1):
            if l[y][x] == "true" and y-x+1>max:
                max = y-x+1
    print max

lps_dp("forgeeksskeegfor")