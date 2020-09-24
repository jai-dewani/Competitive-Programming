for _ in range(int(input())):
	n,r = map(int,input().split())
	ans = 0
	if n<=r:
		ans = (n*(n-1))//2
		ans += 1
	else:
		ans = (r*(r+1))//2
	print(ans)