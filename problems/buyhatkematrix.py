'''
# Read input from stdin and provide input before running code

name = raw_input('What is your name?\n')
print 'Hi, %s.' % name
'''
#print 'Hello World!'
def append(pref,new,th,ex,k,m):

    if th[new]<k and pref==new:
        th[new]+=1
        return
    elif pref!=new and th[new]<k:
        th[new]+=1
        ex[pref]+=1
        return
    else:
        new = find_next(new,th,k,m)
        append(pref,new,th,ex,k,m)

def find_next(new,th,k,m):
    if i==m-1:
        i=0
    else:
        i = new+1
    while(i!=new):
        if i<=m-1 and th[i]<k:
            return i
        if i>=m-1:
            i=0
        else:
            i+=1
            i+=1

junk = raw_input().split()
n = int(junk[0])
m = int(junk[1])
k = int(junk[2])
arr = map(int,raw_input().strip().split())
th = [0]*m
ex = [0]*m

if n-m*k>0:
    i = m*k
else:
    i = n
j=0
while(i>0):
    append(arr[j]-1,arr[j]-1,th,ex,k,m)
    j += 1
    i -= 1

count = 0
for i in xrange(m):
    count+= ex[i]

if n-m*k>0:
    print count+(n-m*k)
else:
    print count

