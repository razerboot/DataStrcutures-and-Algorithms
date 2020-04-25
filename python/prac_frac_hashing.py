def fractionToDecimal(numerator, denominator):
    from collections import OrderedDict
    decimal = 0
    k = 0
    num = numerator
    den = denominator
    if num == 0:
        return 0
    if den == 0:
        return
    if num < 0 and den < 0:
        num *= -1
        den *= -1
    elif num < 0:
        num *= -1
        k = 1
    elif den < 0:
        den *= -1
        k = 1

    r = OrderedDict()
    i = 0
    same=0
    if den > num:
        r[numerator] = "0"
    while (i == 0):
        str1 = ""
        str2 = ""
        if den > num:
            if decimal == 0:
                str1 += "."
                decimal = 1
            num *= 10
            while (den > num):
                str1 += "0"
                num *= 10

        num1 = num % den
        q = (num - num1) / den
        num = num1
        if num1 in r or num1 == 0:
            if num1 != 0:
                str2 = ")"
            i = 1
            num1 = str(num1) + "new"
        r[num1] = str1 + str(q) + str2

        if str(num)+"new"==num1:
            if r[num1] == r[num]+")":
                r[num1] = ")"
                same=1
            elif "." in r[num]:
                split = "0" + r[num].split(".")[1]+")"
                if split == r[num1]:
                    r[num1] = "0)"
                    same=1

    #print r
    str_final = ""
    next1 = 0
    y=1
    for key in r:
        if next1 == 1 or (key == num and same==1):
            if "." in r[key]:
                split = r[key].split(".")
                str_final += ".(" + split[1]
            else:
                str_final += "(" + r[key]
            next1 = 0
            if same==1:
                y=0
        else:
            str_final += r[key]
        if key == num and y==1:
            next1 = 1

    if k == 1:
        return "-" + str_final
    else:
        return str_final
        # return -2%-1

#print fractionToDecimal(826,393)
print fractionToDecimal(23,1176797)


