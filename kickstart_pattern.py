from collections import defaultdict
def create_patterns(s,j,n):
    p=defaultdict(set)
    q=[]
    q.append((s,j,n))
    while(len(q)>0):
        t=q.pop(0)
        n=t[2]
        i=t[1]
        p1=t[0]
        p[n].add(p1)
        while(i<n):
            if p1[i]=="*":
                i1=i+1
                if i1<n:
                    r=p1[i1:]
                else:
                    r=""
                if i==0:
                    l=""
                else:
                    l=p1[:i]
                q.append((l+"****"+r,i+4,n+3))
                q.append((l+"***"+r,i+3,n+2))
                q.append((l+"**"+r,i+2,n+1))
                q.append((l + "*" + r, i + 1, n))
                q.append((l+r,i,n-1))
                break
            i+=1
    return p

def cmpr(ele1,ele2,l):
    for i in xrange(l):
        if ele1[i]!="*" and ele2[i]!="*" and ele1[i]!=ele2[i]:
            return False
    return True
def compare(p1,p2):
    for i in p1:
        ps1=p1[i]
        if len(p2[i])==0:
            continue
        ps2=p2[i]
        for ele1 in ps1:
            for ele2 in ps2:
                if cmpr(ele1,ele2,i):
                    #print ele1,ele2
                    return "True"
    return "False"
t=input()
for x in xrange(t):
    s1=raw_input()
    p_1=s1.split("*")[0]
    l=len(s1)
    #print l
    p1=create_patterns(s1,0,l)
    #print p1
    s2=raw_input()
    l=len(s2)
    #print l
    p2 = create_patterns(s2,0,l)
    #print p2
    print "Case #"+str(x+1)+": "+compare(p1,p2)
