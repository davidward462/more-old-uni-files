#selection sort

A = [1,6,2,8,3,4]

for i in range(len(A)): #i = 0 to (length of A)-1
	minPos = i
	j = i+1
	while(j < len(A)):
		if(A[j] < A[minPos]):
			minPos = j
		j = j+1
	if minPos != i:
		temp = A[i]
		A[i] = A[minPos]
		A[minPos] = temp
		print('swapping', A)
	i = i+1
	print(A)