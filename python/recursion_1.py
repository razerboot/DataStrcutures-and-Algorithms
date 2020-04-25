import math
junk = int(raw_input())
s = raw_input().split()
c = int(raw_input())
array1 = []
seq = [1]

for l in range(0,c):
	array1.append(int(raw_input()))

count = math.log(max(array1)+1,2)-1

#print array1

while count > 0:
	length = len(seq)
	seq = seq+seq
	for x in range(length,2*length):
		seq[x] = seq[x]+int(s[x%junk])
	count = count-1

#print seq
for x in array1:
	print seq[int(x)]

