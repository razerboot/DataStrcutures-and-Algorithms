#for strictly increasing sequence in a array with distinct elements
#ref : www.geeksforgeeks.org/longest-monotonically-increasing-subsequence-size-n-log-n/


def floor(arr, val, l, r):
    while r - l > 1:
        mid = (l + r) / 2
        if arr[mid] <= val:
            l = mid
        else:
            r = mid
    return l


n = input()
arr = map(int, raw_input().split())
# aux array stores last elements of active lists (active lists are of different
#  sizes which can potential candidate for LIS)

aux_arr = [0] * n
l = 0
for i in xrange(n):
    #case 1 - no element in aux array
    if l == 0:
        aux_arr[0] = arr[0]
        l += 1
    else:
        p = floor(aux_arr, arr[i], -1, l)
        # case 2
        # current element is less than all last elements then create a new list of size 1 with current ele
        # this can simulated using aux array by replacing first element with curr element bcoz first element is bigger
        # than curr element if LIS is there from the first element then same LIS can be modified for curr element so it
        # is safe
        if p == -1:
            aux_arr[0] = arr[i]
        # case 3
        # extend the aux array which simulates (we clone largest list and add curr element)
        elif p == l - 1:
            l += 1
            aux_arr[l - 1] = arr[i]
        # case 2
        # clone list corresponding to floor value and add curr element and remove all lists of same size of new list
        # this can simulated by just replacing value in aux arr at p + 1 index
        else:
            aux_arr[p + 1] = arr[i]

print l