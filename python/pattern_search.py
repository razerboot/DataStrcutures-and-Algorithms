#pattern searching through different algorithms


def naive(txt,pat):
    size_p = len(pat)
    size_t = len(txt)
    index = ""
    indices = []
    i = 0
    j = 0
    while i<size_t:
        if j == size_p:
            indices.append(index)
            j =0
            index = ""
        if txt[i] == pat[j]:
            if index=="":
                index = str(i)
            i += 1
            j += 1
        else:
            if index == "":
                i +=1
            else:
                index = ""
                j=0
    if i==size_t:
        if j == size_p:
            indices.append(index)
    print indices


naive("isisis","isi")

