import sys
def clean_p(q):
    n=len(q)
    p=[[False for j in xrange(n)] for i in xrange(n)]
    max_l=1
    for i in xrange(n):
        p[i][i]=True
    for l in xrange(2,n+1):
        for i in xrange(n-l+1):
            j=l+i-1
            b=(q[i]==q[j])
            if l==2:
                p[i][j]=b
            else:
                p[i][j]= b and p[i+1][j-1]
                if p[i][j]:
                    max_l=max(max_l,l)
    #print max_l
    if max_l==1:
        return q
    elif max_l==n:
        if n%2==0:
            return []
        else:
            return [q[(n-1)/2]]
    cut=[0]*n
    c=[0]*n
    for i in xrange(n):
        if p[0][i]:
            c[i]=0
            cut[i]=i
            continue
        c[i] = sys.maxint
        for j in xrange(i):
            if p[j+1][i] and c[i]>1+c[j]:
                c[i]=1+c[j]
                cut[i]=j
    #print p
    #print cut
    #print c
    i=n-1
    n_q=[]
    while 1:
        if cut[i]==i:
            if i%2==0:
                n_q.append(q[i/2])
            break
        else:
            j=cut[i]
            if (i-j)%2!=0:
                n_q.append(q[(i+j+1)/2])
            i=j
    q=n_q[::-1]
    return q

def clean(q):
    while 1:
        q1=clean_p(q)
        if len(q1)==len(q):
            break
        q=q1
        #print q1
    return q1

def dp_top_down(q1,s):
    q=clean(q1)
    mini=None
    n=len(q)
    key=tuple(q)
    if key in s:
        return s[key]
    if len(q)==0:
        return 0
    if len(q)==1:
        return 1
    if len(q)==2:
        if q[0]==q[1]:
            return 0
        else:
            return 2
    for i in xrange(n):
        temp=q[:]
        temp.pop(i)
        if mini==None:
            mini=1+dp_top_down(temp,s)
        else:
            mini=min(mini,1+dp_top_down(temp,s))
    s[key]=mini
    return mini
n=input()
q=map(int,raw_input().split())
s={}
#q=clean_p(q)
#q=clean_p(q)
#print q
#print clean(q)
print dp_top_down(q,s)
print s