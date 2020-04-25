def find_path(num):
    arr = [[0 for i in range(num)] for j in range(num)]
    #positions = [[-2,-1],[-2,1],[-1,-2],[-1,2],[2,-1],[2,1],[1,-2],[1,2]]
    positions = [[2,1],[1,2],[-1,2],[-2,1],[-2,-1],[-1,-2],[1,-2],[2,-1]]
    arr[0][0]=1
    #print 2+positions[2][1]
    print knight_path(arr,0,0,positions,1,num)
    print arr

def check_position(arr,x,y,num):
    if 0<=x<num and 0<=y<num and arr[x][y]==0:
        return True
    return False

def knight_path(arr,x,y,positions,count,num):
    if count==48:
        #arr[x][y] = num * num - count + 1
        return True
    for i in range(8):
        x_pos = x+positions[i][0]
        y_pos = y+positions[i][1]
        if not check_position(arr,x_pos,y_pos,num):
            continue
        arr[x_pos][y_pos] = count+1
        print x_pos,y_pos,count
        if knight_path(arr,x_pos,y_pos,positions,count+1,num):
            return True
        arr[x_pos][y_pos]=0
    return False

find_path(8)