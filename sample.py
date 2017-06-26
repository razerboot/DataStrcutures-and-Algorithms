999 989 975 954 94 949 931 92290390289987285582981780279771757477437437407167157086996636386155895875234624484023893737234232632332231229288286236209196176163124114103
999 989 975 954 949 94 931 92290390289987285582981780279771757477437437407167157086996636386155895875234624484023893737234232632332231229288286236209196176163124114103
def cmpr(a,b):
    a1 = str(a)
    b1 =str(b)
    leng = len(a1)-len(b1)
    if leng==0:
        if b>a:
            return False
    elif leng>0:
        for i in range(len(a1)):
            if i<len(b1):
                tmp_b = b1[i]
            else:
                tmp_b = b1[0]
            if tmp_b>a1[i]:
                return False
            elif tmp_b<a1[i]:
                return True
        if a1[1]<a1[0]:
            return True
        else:
            return False
    elif leng<0:
        for i in range(len(b1)):
            if i<len(a1):
                tmp_a = a1[i]
            else:
                tmp_a = a1[0]
            if b[i]>tmp_a:
                return False
            elif b[i]<tmp_a:
                return True
        if b1[1]<b1[0]:
            return False
        else:
            return True
    return True