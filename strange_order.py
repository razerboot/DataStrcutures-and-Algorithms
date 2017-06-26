
def fact(n,roots):
    r = set()
    sq = int(n ** (0.5))
    for i in roots:
        if n % i == 0:
            r.add(i)
            #roots.remove(i)
    #if n != 1:
    #    r.add(n)

    for i in r:
        roots.remove(i)
    return r


def check(i,roots,primes):
    if primes[i]==0:
        if i in roots:
            return True
        else:
            return False
    for r in roots:
        if i % r == 0:
            return True
    return False

def seive(n,sq1):
    sq = n
    r = set([])
    arr = [0 for i in xrange(sq+1)]
    i=2
    while(i<=sq):
        if arr[i]==0:
            #if i<=sq1:
            r.add(i)
            j=i
            while(j*i<=sq):
                arr[j*i]=1
                j+=1
        i+=1

    return arr,r

n = 10**12
q = [i for i in xrange(10**9)]
sq = int(n ** (0.5))
primes,roots=seive(sq,sq)
q1=[]
arr=[]

#while (len(q) > 0):
#    x = q.pop()
#    r = fact(x,roots)
#    print x,
#    if r != set([x]):
#        while (len(q) > 0):
#            y = q.pop()
#            if check(y,r,primes):
#                print y,
#            else:
#                q1.append(y)
#        q = q1[::-1]
#        q1=[]
#print 1