'''
# Read input from stdin and provide input before running code

name = raw_input('What is your name?\n')
print 'Hi, %s.' % name
'''


# print 'Hello World!'



def cus_sort(a, b):
    l = min(len(a), len(b))
    s = -1
    i = 0
    while (i < l):
        if a[i] == " " and b[i] != " ":
            s = 1
            break
        elif a[i] != " " and b[i] == " ":
            s = -1
            break
        elif a[i].upper() == b[i].upper():
            if b[i] > a[i]:
                s = 1
                break
        else:
            if a[i] > b[i]:
                s = 1
                break
            elif a[i] < b[i]:
                s = -1
                break
        i += 1
    if i == l - 1:
        if len(a) > len(b):
            return 1
        elif len(a) == len(b):
            return 0
        else:
            return -1
    else:
        return s


def sort_arr(arr):
    arr.sort(cmp=cus_sort)
    print arr


t = int(raw_input())
while (t > 0):
    n = int(raw_input())
    arr = []
    while (n > 0):
        stri = raw_input()
        arr.append(stri)
        n -= 1
    #print arr
    sort_arr(arr)
    t -= 1