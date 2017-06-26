from sys import stdin, stdout


def dp(f, matrix, sum_prefix_matrix, sum_array, m, n):
    #matrix[i][j] is count for i selections with last selection as jth type
    # sum_array[i] is count for i selections with any type as last element
    # sum_prefix_matrix[i][j] is prefix count of matrix[i][j] till jth type
    # since we are doing selections we need avoid case like type 2 selection, type 1 selection if already type 1 selection, type 2 selection is there
    # both are same, sum_pefix_matrix is used for that purpose
    mod = 10 ** 9 + 7
    for i in xrange(2, n + 1):
        for j in xrange(m):
            if j == 0:
                matrix[i][j] = sum_array[i - 1]
            else:
                matrix[i][j] = sum_array[i - 1] - sum_prefix_matrix[i - 1][j - 1]
            if i > f[j]:
                matrix[i][j] -= sum_array[i - f[j] - 1] - sum_prefix_matrix[i - f[j] - 1][j]
            sum_array[i] = (sum_array[i] + matrix[i][j]) % mod
            sum_prefix_matrix[i][j] = sum_array[i]


m = input()
f = [0]*m
for a0 in xrange(m):
    f[a0] = input()
q = input()
#buff = stdin.readlines(q)
queries = [0] * q
n = None
for a0 in xrange(q):
    temp = input()
    queries[a0] = temp
    if n == None or n < temp:
        n = temp

sum_prefix_matrix = [[0 for j in xrange(m)] for i in xrange(n + 1)]
matrix = [[0 for j in xrange(m)] for i in xrange(n + 1)]
sum_array = [0 for i in xrange(n + 1)]
sum_array[0] = 1
sum_array[1] = m
for j in xrange(m):
    # doing 1 selection with 1 type of death eater
    matrix[1][j] = 1
    # if there are 1 selection need to made we can do that in way
    sum_prefix_matrix[1][j] = matrix[1][j] + sum_prefix_matrix[1][j - 1]

dp(f, matrix, sum_prefix_matrix, sum_array, m, n)

for k in queries:
    stdout.write(str(sum_array[int(k)]) + '\n')