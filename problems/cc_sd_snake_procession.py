def check_validity(s, l):
    buff = []
    for i in xrange(l):
        if s[i] == 'H':
            if buff == []:
                buff.append(s[i])
            else:
                return 'Invalid'
        elif s[i] == 'T':
            if buff != []:
                buff.pop()
            else:
                return 'Invalid'

    if buff != []:
        return 'Invalid'
    return 'Valid'


n = input()
for a0 in xrange(n):
    l = input()
    s = raw_input()
    print check_validity(s, l)