#l = raw_input()
l = 1
while l>0:
    count1 = 0
    n = 5
    while n!=0:
        n = n & n-1
        count1 = count1+1
    l = l-1
    print count1