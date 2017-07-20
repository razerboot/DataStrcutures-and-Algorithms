import sys
sys.setrecursionlimit(10100)


def grayCode(A):
    arr = []
    arr.append(0)
    get_code(0, arr, A, 1)
    return arr,len(arr)


def check(num1, arr):
    if num1 not in arr:
        return True
    return False


def flip(num, i,N):
    mask = 1 << N-i-1
    return (num ^ mask)


def get_code(num, arr, N, c):
    if c == 2 ** N:
        return True

    for i in range(N):
        num1 = flip(num, i,N)
        if check(num1, arr):
            arr.append(num1)
            if get_code(num1, arr, N, c + 1):
                return True
            arr.pop()
    return False


def grayCode1(A):
    arr = [0, 1]
    find_arr(arr,1, 1, A)
    return arr


def find_arr(arr,xor,p,c):
    if p==c:
        return
    size = 2**p
    add = 2**p
    for i in range(size):
        arr.append((arr[i]^xor)+add)
    find_arr(arr,xor+add,p+1,c)
    return

print grayCode1(3)

#print 2^3+2**2