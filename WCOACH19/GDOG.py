t = int(input())
for z in range(t):
	n,k = list(map(int,input().split()))
	temp = n//2
	temp += 1
	if k>n:
		print(n)
	elif temp<=k:
		print(n%temp)
	else:
		#print("three")
		ans = 0
		for i in range(1,k+1):
			if ans<(n%i):
				ans = n%i
		print(ans)