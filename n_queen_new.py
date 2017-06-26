
# print 'Hello World!'
N = int(raw_input())
q = N
board = [["." for x in range(N)] for y in range(N)]
arr = []

def check_pos(board, x, y):
    for h in range(N):
        if board[h][x] == "Q":
            return False
    for w in range(N):
        if board[y][w] == "Q":
            return False

    for h in range(N):
        for w in range(N):
            if abs(x - w) == abs(y - h):
                if board[h][w] == "Q":
                    return False
    return True

def create_string(board):
    str2 = []
    for h in range(N):
        str1 = ''
        for w in range(N):
                str1 += str(board[h][w])
        str2.append(str1)
    return str2

def place(board, q,h):
    if q == 0:
        str1 = create_string(board)
        arr.append(str1)
        return
    if h>N:
        return
    for w in range(N):
        if check_pos(board, w, h):
            board[h][w] = "Q"
            place(board, q - 1,h+1)
            board[h][w] = "."
    return

place(board, q,0)
if arr!=[]:
    print arr


