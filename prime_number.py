
# normal method
def check_prime(num):
    sq_rt = int(num**(.5))
    for i in range(2,sq_rt+1):
        if num%i == 0:
            return i
    return "true"
    #print sq_rt

#print check_prime(1973)

#Sieve of Eratosthenes

def check_prime_1(num):
    sq_rt = int(num**(0.5))
    arr = [0]*(sq_rt+1)
    i = 2
    while(i<=sq_rt):
        if arr[i] == 0:
            j = i*i
            while i*j<=sq_rt:
                arr[i*j] = 1
                j += 1
        i += 1

    #for i in range(2,len(arr)):
     #   if arr[i] == 0:
     #       if num%i == 0:
     #           return i
    return arr

#print check_prime_1(1973)

def factorize(num):
    arr = []
    i =2
    while(i*i<=num):
        while(num%i == 0):
            arr.append(i)
            num /= i
        i += 1

    if num != 1:
        arr.append(num)
    return arr

# seive of Eratosthenes on a segment
def segmented_seive(lo,hi):
    arr = check_prime_1(hi)
    arr1 = [0]*(hi-lo+1)
    i =2
    while i*i<=hi:
        if arr[i] == 0:
            j = max(i,1+(f-f%i)/i)
            while i*j<=hi:
                arr1[i*j-lo] = 1
                j += 1
        i += 1
    for i in range(hi-lo+1):
        if arr1[i] == 0:
            print lo+i

segmented_seive(97,200)

def seive(n):
    sq = n
    r = set([])
    arr = [0 for i in xrange(sq+1)]
    i=2
    while(i<=sq):
        if arr[i]==0:
            r.add(i)
            j=i
            while(j*i<=sq):
                arr[j*i]=1
                j+=1
        i+=1

    return arr

