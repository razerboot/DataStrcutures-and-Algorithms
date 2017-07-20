#use in hacker rank
#a = map(int, raw_input().strip().split(' '))
# my_dict.keys()
#get keys in the form of list
# my_dict.pop("key",None)
# delete the key and if key is not found return None(we can customize it)

def lps(str):
    N = len(str)
    #size is last position in the new string 1
    size = 2*N
    str1 = ""
    l = [0]*(size+1)
    for i in range(N):
        if i==0:
            str1 = "#"+str[i]+"#"
        else:
            str1 += str[i]+"#"
    crs = 2
    c_p = 1
    i=2
    l[1]=1
    #algo
    while(i<=size):
        if i<=crs:
            i_l = 2*c_p-i
            m = crs-i
            # case 1
            if l[i_l]<m:
                l[i] = l[i_l]
            # case 2
            if l[i_l]>=m and crs==size:
                l[i] = m
            # case 3 and 4
            if l[i_l]>=m and crs<size:
                l[i] = m
                while(crs+1<=size and 2*i-(crs+1)>=0 and str1[2*i-(crs+1)]==str1[crs+1]):
                    crs += 2
                    l[i] += 2
                if crs>m+i:
                    c_p = i
        else:
            #print "fk"
            crs=i
            c_p = i
            while (crs + 1 <= size and 2*i-(crs+1)>=0 and str1[2 * i - (crs + 1)] == str1[crs + 1]):
                crs += 1
                l[i] += 1
        i += 1

    # printing the longest palindrome substring
    i = 0
    d = 0
    for j in range(size+1):
        if l[j]>d:
            d = l[j]
            i = j
    str2 = ""
    for j in range((i-d)/2,(i+d)/2):
        str2 += str[j]
    print l
    print str
    print str2

lps("cdabccc")