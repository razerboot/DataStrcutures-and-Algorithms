# the trick when a substring is a prefix we will use the matching pattern of this substring in the iteration
#join the patt with text with any special character
def z_algo(txt,pat):
    z_txt = pat+"#"+txt
    l = 0
    r = 0
    z = [0]*len(z_txt)
    i = 1
    while (i<len(z_txt)):
        if i>r:
            j = z_comp(len(pat),z_txt,i)
            l = i
            r = i+j-1
            z[i] = j
        else:
            if z[i-l]<r-i+1:
                z[i] = z[i-l]
            else:
                while(r<len(z_txt) and z_txt[r+1] == z_txt[r-i+1]):
                    r += 1
                l = i
                z[i] = r-l+1
        i +=1
    return z

def z_comp(k,z_txt,i):
    j=0
    while(i<len(z_txt) and j<k):
        if z_txt[j] != z_txt[i+j]:
            break
        j += 1
    return j

print z_algo("ABABABA","ABA")