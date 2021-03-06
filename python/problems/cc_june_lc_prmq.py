from collections import defaultdict, Counter
from random import randrange
from time import time


def cal_prefix_counters(arr, primes, prefix_counters, counters, n):
    '''for each number in arr we factorize them using primes'''
    maxi = max(arr)
    for p in primes:
        if p * p > maxi:
            break
        for i in xrange(n):
            while arr[i] % p == 0:
                arr[i] /= p
                counters[i][p] += 1

    for i in xrange(n):
        if arr[i] != 1:
            counters[i][arr[i]] += 1

    '''we preprocess prefix counters'''
    prefix_counters[0] = counters[0]
    for i in xrange(1, n):
        prefix_counters[i] = prefix_counters[i - 1] + counters[i]


def seive(n):
    vi = [0 for i in xrange(n + 1)]
    p = []
    i = 2
    while i * i <= n:
        if vi[i] == 0:
            j = i
            while i * j <= n:
                vi[i * j] = 1
                j += 1
        i += 1
    for i in xrange(2, n + 1):
        if vi[i] == 0:
            p.append(i)
    return p


# n = 1000
# q = 10000
# arr = [randrange(1, 10 ** 6) for i in xrange(n)]

n = input()
#arr = map(int, raw_input().split())
arr = [28166, 478575, 99579, 180446, 921100, 460918, 195496, 979215, 781528, 567092, 402360, 385434, 310877, 660660, 468827, 888862, 909673, 479247, 147056, 728727, 880209, 456368, 193909, 384841, 786944, 877475, 802531, 415708, 876023, 283156, 123061, 679540, 958206, 377649, 801583, 610609, 325518, 821373, 717170, 133869, 696334, 111478, 490470, 659323, 325159, 633984, 922096, 974317, 848843, 503536, 375711, 450261, 515160, 721309, 815518, 542774, 312038, 77730, 129342, 937235, 975980, 341779, 827639, 676112, 611687, 240700, 848053, 831590, 286938, 540735, 449384, 431449, 855677, 363894, 115385, 971355, 47064, 192164, 538186, 954486, 687467, 590080, 42486, 943119, 172974, 327917, 890411, 775027, 768895, 478660, 751327, 313037, 930894, 782509, 393324, 931940, 595395, 810785, 427174, 102373, 76988, 885567, 108231, 488708, 995495, 45331, 758788, 404072, 574800, 456232, 625951, 936214, 621563, 363377, 290414, 974692, 81502, 924860, 882803, 496791, 298095, 589263, 777393, 187916, 60224, 337031, 479328, 912600, 391719, 462324, 811521, 499378, 856399, 935940, 216265, 465817, 699756, 78990, 696739, 105474, 380833, 663005, 782312, 322411, 437775, 341307, 538940, 961126, 647857, 428868, 934874, 676938, 995454, 293065, 709837, 925176, 307764, 877939, 878858, 689575, 323588, 147692, 825979, 222464, 907248, 465237, 363551, 77515, 268069, 424583, 848439, 795725, 558912, 476190, 75832, 896060, 729574, 741227, 355880, 172990, 852657, 65227, 616059, 873317, 674392, 53834, 792648, 613735, 870977, 137054, 280538, 608020, 314916, 241468, 686889, 921141, 814903, 451104, 950347, 414799, 551866, 318455, 321356, 324667, 858834, 215458, 272630, 905618, 255304, 456859, 445100, 574269, 164190, 450114, 142972, 549354, 499829, 608941, 163107, 474853, 779556, 843931, 425906, 612506, 309303, 80172, 49767, 592164, 215239, 856869, 220442, 893614, 640227, 197323, 393247, 765552, 319610, 975304, 741782, 54706, 576765, 989727, 454886, 757818, 760553, 25685, 569525, 960829, 495926, 331857, 247747, 452855, 395321, 937706, 290276, 829414, 830702, 291340, 70452, 437222, 174173, 687492, 413814, 696240, 8832, 101344, 300139, 686189, 133616, 461922, 844636, 752971, 70716, 13385, 226471, 854319, 430898, 544434, 701627, 517886, 59129, 638878, 521857, 869623, 994584, 185323, 892031, 791578, 971946, 321634, 369919, 169657, 249236, 735734, 176238, 252377, 377373, 695618, 999858, 157071, 119579, 609847, 578618, 214107, 679616, 728160, 722932, 909705, 952348, 75540, 672761, 141867, 137671, 520746, 752989, 820758, 39123, 567876, 892909, 146223]
q = input()
primes = seive(10 ** 3)

counters = defaultdict(Counter)
prefix_counters = defaultdict(Counter)

t1 = time()
cal_prefix_counters(arr, primes, prefix_counters, counters, n)

# print time() - t1

t2 = time()
for a0 in xrange(q):
    # l = randrange(n)
    # r = randrange(l, n)
    # x = randrange(2, 10 ** 6 + 1)
    # y = randrange(x, 10 ** 6 + 1)
    l, r, x, y = map(int, raw_input().split())
    l -= 1
    r -= 1
    if l != 0:
        c = prefix_counters[r] - prefix_counters[l - 1]
    else:
        c = prefix_counters[r]
    count = 0
    for key in c:
        if x <= key <= y:
            count += c[key]
    print count
    # print time() - t2