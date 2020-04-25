# gcd of two numbers based on euclidean algorithm
import math
def gcd(a,b):
    if a==0:
        return b

    return gcd(b%a,a)

# extended gcd to calculate multiplicative modulo inverse
def gcd_extended(a,b,arr):
    if a==0:
        x=0
        y=1
        arr[0]=b
        arr[1] = x
        arr[2] = y
        return arr

    junk = gcd_extended(b%a,a,arr)
    gcd = junk[0]
    x1 = junk[1]
    y1 = junk[2]
    x = y1 - math.floor(b/a)*x1
    y = x1
    arr[0] = gcd
    arr[1] = x
    arr[2] = y
    return arr
arr = [-1,-1,-1]
print gcd_extended(35,15,arr)