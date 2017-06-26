
# bot up dp
def lcs_bt_up(s1,s2):
    l1=len(s1)
    l2=len(s2)
    c=[[-1 for j in xrange(l1+1)] for i in xrange(l2+1)]
    for j in xrange(l1+1):
        c[0][j]=0
    for i in xrange(l2+1):
        c[i][0]=0
    for i in xrange(1,l2+1):
        for j in xrange(1,l1+1):
            if s1[j-1]==s2[i-1]:
                c[i][j]=c[i-1][j-1]+1
            elif c[i-1][j]>=c[i][j-1]:
                c[i][j]=c[i-1][j]
            else:
                c[i][j]=c[i][j-1]
    return c

def print_lcs(s2,s1,c,i,j):
    if i==0 or j==0:
        return
    if s2[i-1]==s1[j-1]:
        print_lcs(s2,s1,c,i-1,j-1)
        print s2[i-1],
    elif c[i][j]==c[i][j-1]:
        print_lcs(s2,s1,c,i,j-1)
    else:
        print_lcs(s2,s1,c,i-1,j)

#top-down dp
def top_dwn(c,s1,s2,i,j):
    if i==0 or j==0:
        return 0
    if c[i][j]!=-1:
        return c[i][j]
    if s1[j-1]==s2[i-1]:
        c[i][j]=1+top_dwn(c,s1,s2,i-1,j-1)
        return c[i][j]
    else:
        c[i][j]=max(top_dwn(c,s1,s2,i-1,j),top_dwn(c,s1,s2,i,j-1))
        return c[i][j]


s1="BDCABA"
s2="ABCBDAB"

c = lcs_bt_up(s1,s2)
print c
print_lcs(s2,s1,c,len(s2),len(s1))
l1=len(s1)
l2=len(s2)
c=[[-1 for j in xrange(l1+1)] for i in xrange(l2+1)]
print top_dwn(c,s1,s2,len(s2),len(s1))
print c
print_lcs(s2,s1,c,len(s2),len(s1))