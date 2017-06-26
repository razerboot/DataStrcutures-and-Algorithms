

t = input()
for a0 in xrange(t):
    s1 = raw_input()
    c = {}
    c['C'] = 1
    c['E'] = 2
    c['S'] = 3
    prev = None
    for ele in s1:
        if prev is None:
            prev = ele
        else:
            if c[prev] > c[ele]:
                print 'no'
                break
            prev = ele
    else:
        print 'yes'