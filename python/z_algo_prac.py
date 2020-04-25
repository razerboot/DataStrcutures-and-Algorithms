def z_algo(txt,pat):
    i=1
    l=0
    r=0
    z_txt = pat+"#"+txt
    size = len(z_txt)
    z = [0]*size
    z[0] = -1
    while(i<size):
        if i>r:
            l=i
            r=i
            while(r<size and z_txt[r]==z_txt[r-l]):
                r += 1
            z[i] = r-l
            r -= 1
        else:
            if z[i-l]<r-i+1:
                z[i] = z[i-l]
            else:
                l=i
                #z[i]=r-i+1
                r += 1
                while(r<size and z_txt[r]==z_txt[r-l]):
                    r += 1
                z[i]= r-l
                r -= 1
        i += 1
    return z

print z_algo("EGEEGEEG","EGEEG")
