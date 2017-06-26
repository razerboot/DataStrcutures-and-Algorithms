A=raw_input()
B=input()
A = A.strip()
n = len(A)
# print n
bw = [(0, 0)] * n
if B > n:
	print -1
elif B == n:
	print 0
for j in xrange(n):
	if j == 0:
		if A[j] == "B":
			bw[j] = (1, 0)
		else:
			bw[j] = (0, 1)
	else:
		b, w = bw[j - 1]
		if A[j] == "W":
			w += 1
		else:
			b += 1
		bw[j] = (b, w)
# print bw
mat = [[-1 for j in xrange(n)] for i in xrange(B)]
for i in xrange(B):
	mat[i][i] = 0
for i in xrange(B):
	for j in xrange(i + 1, n):
		bj, wj = bw[j]
		if i == 0:
			mat[i][j] = bj * wj
		else:
			for k in xrange(i - 1, j):
				bk, wk = bw[k]
				s = mat[i - 1][k] + (bj - bk) * (wj - wk)
				if mat[i][j] == -1:
					mat[i][j] = s
				else:
					mat[i][j] = min(mat[i][j], s)
print mat
print mat[B-1][n - 1]

