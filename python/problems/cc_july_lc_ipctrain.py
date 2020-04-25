import heapq as pq
from collections import defaultdict


t = input()
for a0 in xrange(1, t + 1):
    N, D = map(int, raw_input().split())
    d_list = defaultdict(list)
    for a1 in xrange(N):
        Di, Ti, Si = map(int, raw_input().split())
        d_list[Di].append((-1 * Si, Ti))
    heap = []
    ans = 0
    for i in xrange(1, D + 1):
        for ele in d_list[i]:
            pq.heappush(heap, ele)
        while heap:
            ele = pq.heappop(heap)
            if ele[1] > 1:
                ans += ele[0]
                pq.heappush(heap, (ele[0], ele[1] - 1))
                break
            elif ele[1] == 1:
                ans += ele[0]
                break
    for k in d_list:
        for ele in d_list[k]:
            ans += -1 * ele[0] * ele[1]
    print ans
