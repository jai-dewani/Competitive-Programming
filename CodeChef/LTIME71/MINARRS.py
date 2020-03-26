import math
t = int(input())
for _ in range(t):
	n = int(input())
	array = [int(x) for x in input().split()]	
	large = max(array)
	large = len(bin(large))-2
	# totalOne = {}
	# for i in range(32):
	# 	totalOne[i] = 0

	totalOne = [0 for i in range(large)]
	
	for i in range(len(array)):
		temp = bin(array[i])[2:]
		l = len(temp)
		for i in range(l):
			totalOne[i]+=int(temp[l-i-1])
		# temp = array[i]
		# i = 0
		# while temp:
		# 	totalOne[i] += temp%2
		# 	temp = temp//2
		# 	i+=1
	# print(totalOne)
	number = ''
	for i in range(len(totalOne)):
		if totalOne[i]>n//2:
			number = '1'+ number 
		else:
			number = '0'+number

	# print(number)	
	# for i in totalOne:
	# 	if i>n//2:
	# 		number = '1' + number 
	# 	else:
	# 		number = '0' + number
	number = int(number,base=2)
	for i in range(len(array)):
		array[i] = array[i]^number
	print(sum(array))

	# ar = []
	# for i in range(len(array)):
	# 	temp = bin(array[i])[2:]
	# 	temp = '0'*(large-len(temp))+temp
	# 	ar.append(temp)
	# 	for j in range(len(ar[i])-1,-1,-1):
	# 		totalOne[j]+=int(ar[i][j])
	# number = ''
	# for i in totalOne:
	# 	if i>n//2:
	# 		number = number+'1'
	# 	else:
	# 		number = number+'0'
	# number = int(number,base=2)
	# for i in range(len(ar)):
	# 	array[i] = array[i]^number
	# print(totalOne)
	# print(ar)
	# print(array,number)
	# print(sum(array))

