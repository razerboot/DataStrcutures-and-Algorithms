array1 = [1,2,3,4,5,7,4,9]
position=5
value = 34
length = len(array1)
j = length-1

# insertion
def insertion(array1,position,length):
	while j>=position-1:
		#print array1[j]
		if j+1 == length:
			array1.append(array1[j])
		else:
			array1[j+1]=array1[j]
		j = j-1
	array1[position-1]=value



# deletion
def deletion(array1,position,length):
	j = position - 1
	while j<=length:
		if j == length:
			print array1[j]
		else:
			array1[j] = array1[j+1]
		j = j+1

#s