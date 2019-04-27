t = int(input())
for _ in range(t):
	n = int(input())
	A = [int(x) for x in input().split()]
	B = [int(x) for x in input().split()]
	B.reverse()
	temp1 = 0
	temp2 = 0
	sumA = [0]
	sumB = [0]
	for i in range(len(A)):
		temp1 += A[i]
		temp2 += B[i]
		sumA.append(temp1)
		sumB.append(temp2)
	sumB.reverse()
	ans = 0
	for i in range(len(A)+1):
		ans = max(ans,sumA[i]+sumB[i])
	# print(sumA)
	# print(sumB)
	print(ans)