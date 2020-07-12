for _ in range(int(input())):
	n = int(input())
	# n,m = map(int,input().split())
	ar = list(map(int,input().split()))
	index = [-1]*n 
	count = 0
	temp = 0
	for i in range(n):
		if ar[i]!=i+1:
			if temp==0:
				count += 1
			temp += 1
			index[i] = ar[i]-1 
		else:
			temp = 0
	if count==0:
		print(0)
	elif count==1:
		print(1)
	else:
		print(2)
	# print(index)
	
	