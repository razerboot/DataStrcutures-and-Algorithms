'''
# Read input from stdin and provide input before running code

name = raw_input('What is your name?\n')
print 'Hi, %s.' % name
'''
#print 'Hello World!'
counter = {}
counter[1]=[[1,1]]
counter[2]=[[2,1]]
counter[3]=[[3,1]]
counter[4]=[[2,2]]
counter[5]=[[5,1]]
counter[6]=[[2,1],[3,1]]
counter[7]=[[7,1]]
counter[8]=[[2,3]]
counter[9]=[[3,2]]
counter[10]=[[5,1],[2,1]]

ref = {}
ref[2]=0
ref[3]=0
ref[5]=0
ref[7]=0

def get_count(arr,i,j,mo,oper):
    for k in xrange(i,j+1):
        if arr[k]!=1:
            c = counter[arr[k]]
            if len(c)==1:
                if ref[c[0][0]]>=0:
                    ref[c[0][0]]=(eval(str(ref[c[0][0]])+oper+str(c[0][1])))%mo
                    if ref[c[0][0]]<0:
                        ref[c[0][0]]=0
            else:
                if ref[c[0][0]]>=0:
                    ref[c[0][0]]=(eval(str(ref[c[0][0]])+oper+str(c[0][1])))%mo
                    if ref[c[0][0]]<0:
                        ref[c[0][0]]=0
                if ref[c[1][0]]>=0:
                    ref[c[1][0]]=(eval(str(ref[c[1][0]])+oper+str(c[1][1])))%mo
                    if ref[c[1][0]]<0:
                        ref[c[1][0]]=0
def cal_count():
    count=1
    for ele in ref:
        if ref[ele]>0:
            count = (count*(ref[ele]+1))%mo
    return count
junk = raw_input().split()
n = int(junk[0])
m = int(junk[1])
arr = map(int, raw_input().strip().split())
prev = {}
mo = 10**9+7
prev_i=-1
prev_j=-1

while(m>0):
    junk = raw_input().split()
    i = int(junk[0])-1
    j = int(junk[1])-1
    key = str(i)+"#"+str(j)
    if key in prev:
        print prev[key]
    else:
        if i>prev_j or prev_i>j:
            get_count(arr,i,j,mo,"+")
        elif prev_i>=i and prev_j<=j:
            if prev_i>i:
                get_count(arr,i,prev_i-1,mo,"+")
            if j>prev_j:
                get_count(arr,prev_j+1,j,mo,"+")
        elif i>=prev_i and j<=prev_j:
            if i>prev_i:
                get_count(arr,prev_i,i-1,mo,"-")
            if prev_j>j:
                get_count(arr,j+1,prev_j,mo,"-")
        elif i>prev_i and j>prev_j:
            get_count(arr,prev_i,i-1,mo,"-")
            get_count(arr,prev_j+1,j,mo,"+")
        elif prev_i>i and prev_j>j:
            get_count(arr,i,prev_i-1,mo,"+")
            get_count(arr,j+1,prev_j,mo,"-")
        else:
            get_count(arr,i,j,mo,"+")
        prev_i=i
        prev_j=j
        value = cal_count()
        prev[key]=value
        print value

    m-=1







