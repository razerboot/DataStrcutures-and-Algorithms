'''
# Read input from stdin and provide input before running code

name = raw_input('What is your name?\n')
print 'Hi, %s.' % name
'''
import array
from collections import defaultdict
import operator
t = int(raw_input())
def less_to_high(arr,st):
    size = len(st)
    for ele in st:
        arr[ele][1]+=1
    print arr
    arr1 = sorted(arr.itervalues(),key=operator.itemgetter(1,0))
    print arr1
    #arr2 = sorted(arr1,key=operator.itemgetter(1))
    ls = [chr(k[0]*-1) for k in arr1]
    str1 = " ".join(ls)
    return str1


for i in xrange(t):
    alpha = "zyxwvutrsqponmlkjihgfedcba"
    arr = {}
    for ele in alpha:
        arr[ele] = [(-1*ord(ele)),0]
    st = raw_input()
    print less_to_high(arr,st)



