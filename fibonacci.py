#fibonacci number at index [a] while storing at each index in a array
def feb(a,b):
    if b[a] == -1:
        if a==0:
            return 0
        if a==1:
            return 1
        return feb(a-1,b)+feb(a-2,b)
    else:
        return b[a]
#at index [a] while storing only previous 2
#def feb_1(a,b1):

fib_ind = 9
b=[-1]*fib_ind
#print feb(fib_ind-1,b)

def check_fib(a):
    m=1
    n=1
    index = 3
    fib=0
    if a==1:
        return 2
    elif a==0:
        return 1
    else:
        while(fib<a):
            fib = n+m
            m = n
            n= fib
            index += 1
        if fib == a:
            return index
        else:
            return "sorry not a fib"

print check_fib(21)
