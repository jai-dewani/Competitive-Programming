for _ in range(int(input())):
	a,b,n,m = map(int,input().split())
	ans = -1
	if a+b<n+m:
		ans = 0 
	else:
		if min(a,b)>=m:
			ans = 1
		else:
			ans = 0 
	if ans:
		print("Yes")
	else:
		print("No")