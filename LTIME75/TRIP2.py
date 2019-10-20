t = int(input())
for _ in range(t):
	n,k = list(map(int,input().strip().split()))
	ar = list(map(int,input().strip().split()))
	if k>2:
		if ar[0]==-1:
			if ar[1]==1:
				ar[0] = 0
			else:
				ar[0] = 0
		if ar[n-1]==-1:
			if ar[n-2]==1:
				ar[n-1] = 0
			else:
				ar[n-1] = 1
		for i in range(1,n-1):
			if ar[i]==-1:
				ar[i] = ar[i-1]^ar[i+1]

		print("YES")
		print(*ar)
	elif k==2:
		flag = True
		found = -1
		for i in range(n):
			if ar[i]!=-1:
				found = i
				break
		if found!=-1:
			for i in range(found+1,n):
				ar[i] = 3-ar[i-1]
			for i in range(found-1,-1,-1):
				ar[i] = 3-ar[i+1]
			for i in range(n-1):
				if ar[i]==ar[i+1]
		else:
			ar[0] = 1
			for i in range(n):
				ar[i] = 3-ar[i-1]
			print("YES")
			print(*ar)
		if flag:
			for i in range(1,n):
				if ar[i]==-1:
					ar[i] = 3-ar[i-1]
			print("YES")
			print(*ar)
		else:
			print("NO")
	else:
		print("NO")