def solve_sudoko():
    grid = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
           [5, 2, 0, 0, 0, 0, 0, 0, 0],
           [0, 8, 7, 0, 0, 0, 0, 3, 1],
           [0, 0, 3, 0, 1, 0, 0, 8, 0],
           [9, 0, 0, 8, 6, 3, 0, 0, 5],
           [0, 5, 0, 0, 9, 0, 6, 0, 0],
           [1, 3, 0, 0, 0, 0, 2, 5, 0],
           [0, 0, 0, 0, 0, 0, 0, 7, 4],
           [0, 0, 5, 2, 0, 6, 3, 0, 0]]
    x=0
    y=0
    c = count_zeroes(grid)
    print solve(grid,x,y,c)
    print grid

def count_zeroes(grid):
    count=0
    for i in range(9):
        for j in range(9):
            if grid[i][j]==0:
                count+=1
    return count

def get_next(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j]==0:
                return i,j

def check(grid,x,y,num):
    a1 = x-x%3
    b1 = y-y%3
    a = a1,a1+1
    b = b1,b1+1
    # checking in row
    for j in range(9):
        if grid[x][j]==num:
            return False
    #checking in column
    for i in range(9):
        if grid[i][y]==num:
            return False
    #checking in subgrid
    for i in range(a[0],a[1]):
        for j in range(b[0],b[1]):
            if grid[i][j]==num:
                return False
    return True

def solve(grid,x,y,c):
    if c==0:
        print grid
        return True
    next1 = get_next(grid)
    #print next1
    x_nxt = next1[0]
    y_nxt = next1[1]
    for i in range(1,10):
        if check(grid,x_nxt,y_nxt,i):
            grid[x_nxt][y_nxt] = i
            if solve(grid,x_nxt,y_nxt,c-1):
                return True
            grid[x_nxt][y_nxt] = 0

    return False

solve_sudoko()