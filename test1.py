l = int(raw_input())
k = 20000
Matrix = [[0 for x in range(l)] for y in range(l)]

def check_position(x,y):
    for x1 in range (0,l):
        if Matrix[x1][y] == 1:
            return 0
    for y1 in range(0,l):
        if Matrix[x][y1] == 1:
            return 0
    for x1 in range(0,l):
        for y1 in range(0,l):
            if abs(x-x1) == abs(y-y1):
                if Matrix[x1][y1] == 1:
                    return 0
    return 1

def add_position(n,k):
    k = k-1
    if k == 0:
        return "Not possible"
    if n == 0:
        return 1
    for i in range(0,l):
        for j in range(0,l):
            if Matrix[i][j]!=1 and check_position(i,j) ==1:
                Matrix[i][j] =1
                if add_position(n-1,k) == 1:
                    return 1
                Matrix[i][j] = 0
    return "Not possible"

def printer():
    for y in range(0,l):
        string = ""
        for x in range (0,len(Matrix[y])):
            if string == "":
                string = str(Matrix[y][x])
            else:
                string = string+" "+str(Matrix[y][x])
        print string
        print "\n"

if add_position(l,k) == "Not possible":
    print "Not possible"
else:
    printer()