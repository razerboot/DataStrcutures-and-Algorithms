
array = [10,23,53,76,84,95]

array1 = [1,2,3,4,5]

def bs(array,a,b,input):
    size = b+a
    mid = (size-size%2)/2
    if input == array[mid]:
        return mid
    if b-a<=1:
        return -1
    if input>array[mid]:
        a = mid
    else:
        b= mid
    return bs(array, a, b, input)

def is_i(array,a,b,input):
    lo = a
    hi = b
    while(hi>=lo):
        pos = lo+((input-array[lo])*(hi-lo)/(array[hi]-array[lo]))
        if array[pos] == input:
            return pos
        if input>array[pos]:
            a = pos+1
        else:
            b = pos-1
    return -1

def bs_i_left(array,a,b,input):
    while(b-a>1):
        size = b+a
        mid = (size-size%2)/2
        if input>array[mid]:
            a = mid
        else:
            b = mid

    if array[b] == input:
        return b
    else:
        return -1


def bs_i_right(array,a,b,input):

    while(b-a>1):
        size = b+a
        mid = (size-size%2)/2
        if input>=array[mid]:
            a = mid
        else:
            b = mid

    if array[a] == input:
        return a
    else:
        return -1

def pulse(array,a,b):

    if array1[a]<array1[b-1]:
        return array1[a]

    while (b-a>1):
        size = a+b
        mid = (size-size%2)/2
        if array[mid]>array[a]:
            a = mid
        else:
            b = mid

    return array[b]


#print pulse(array1,0,len(array))
#print is_i(array,0,len(array)-1,10)
#print bs_i_right(array,0,len(array),53)-bs_i_left(array,0,len(array),53)+1
a={}
a = set()
a.add(1)
a.add(2)
a.add(3)
print a