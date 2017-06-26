def read(type=int):
    return type(input())


def read_arr(type=int):
    return [type(token) for token in raw_input().split()]

M = 2002
N = 2002
ADP = [x[:] for x in [[0] * (M + 1)] * (N + 1)]
CDP = [x[:] for x in [[0] * (M + 1)] * (N + 1)]
SDP = [0] * (N + 1)

def solution_optimal(n, m, T):
    for j in range(m):
        ADP[0][j] = 1
        CDP[0][j] = 0

    for i in range(1, n + 1):
        SDP[i] = 0
        for j in range(m):
            lim = min(i, T[j])
            CDP[i][j] = (CDP[i - 1][j] + ADP[i - 1][j]) % mod
            if i >= lim + 1:
                CDP[i][j] = (CDP[i][j] - ADP[i - lim - 1][j] + mod) % mod
            SDP[i] = (SDP[i] + CDP[i][j]) % mod

        for j in range(m):
            ADP[i][j] = (SDP[i] - CDP[i][j] + mod) % mod
    return SDP[n]


mod = 10 ** 9 + 7
t = read()
for i in range(t):
    n, e = read_arr()
    K = read_arr()
    ans = solution_optimal(n, e, K)
    print(ans)
