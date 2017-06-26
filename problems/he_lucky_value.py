import random

def dp(matrix, row_suffix_matrix, column_suffix_matrix, n, m):
    for i in xrange(n):
        for j in reversed(xrange(m)):
            if i == 0 and j == m - 1:
                row_suffix_matrix[0][m - 1] = matrix[0][m - 1]
                column_suffix_matrix[0][m - 1] = matrix[0][m - 1]
            else:
                maxi = matrix[i][j]
                if j + 1 < m and matrix[i][j] + row_suffix_matrix[i][j + 1] > maxi:
                    maxi = matrix[i][j] + row_suffix_matrix[i][j + 1]

                if i - 1 >= 0 and maxi < matrix[i][j] + column_suffix_matrix[i - 1][j]:
                    maxi = column_suffix_matrix[i - 1][j] + matrix[i][j]

                if j + 1 < m:
                    row_suffix_matrix[i][j] = max(maxi, row_suffix_matrix[i][j + 1])
                else:
                    row_suffix_matrix[i][j] = maxi
                if i - 1 >= 0:
                    column_suffix_matrix[i][j] = max(row_suffix_matrix[i][j], row_suffix_matrix[i - 1][j])
                else:
                    column_suffix_matrix[i][j] = row_suffix_matrix[i][j]

    #print column_suffix_matrix
    #print row_suffix_matrix

    return column_suffix_matrix[n - 1][0]


t = input()
for a0 in xrange(t):
    n, m = map(int, raw_input().split())
    matrix = [[0 for j in xrange(m)] for i in xrange(n)]
    row_suffix_matrix = [[0 for j in xrange(m)] for i in xrange(n)]
    column_suffix_matrix = [[0 for j in xrange(m)] for i in xrange(n)]

    for a1 in xrange(n):
        #temp = map(int, raw_input().split())
        for a2 in xrange(m):
            #matrix[a1][a2] = temp[a2]
            matrix[a1][a2] = random.randrange(-1 * 10 ** 6, 10 ** 6)

    print dp(matrix, row_suffix_matrix, column_suffix_matrix, n, m)
