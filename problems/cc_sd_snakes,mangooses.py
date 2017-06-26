t = input()
for a0 in xrange(t):
    s = raw_input()
    n = len(s)
    csnake = 0
    cmongoose = 0
    for i in xrange(n):
        if s[i] == 's':
            csnake += 1
        else:
            cmongoose += 1
    not_eatten = 1
    is_snake = 0
    for i in xrange(n):
        if s[i] == 'm':
            l = i - 1
            r = i + 1
            if l >= 0 and s[l] == 's' and not_eatten == 1:
                csnake -= 1
            elif r < n and s[r] == 's':
                csnake -= 1
                not_eatten = 0
            is_snake = 0
        elif s[i] == 's' and is_snake == 1:
            not_eatten = 1
        else:
            is_snake = 1


    if csnake == cmongoose:
        print 'tie'
    elif csnake > cmongoose:
        print 'snakes'
    else:
        print 'mongooses'