#sorting

def sorting(arr,n):
    import operator
    arr.sort(key=operator.itemgetter(n))
    return arr



print sorting([[1,2,3],[3,1,5],[6,0,1]],0)

# default dict for default values
# from collections import defaultdict
#sorting for dictionary
#d1 = sorted(d.items(),key=operator.itemgetter(0),reverse=True)
#d = defaultdict(int) int,list,set
#for k,v in crate:
#    d[v] += k


#python array module
#python operator
