for _ in range(int(input())):
	# n = int(input())
	n,b,m = map(int,input().split())
	ar = list(map(int,input().split()))
	cur = -1
	ans = 0
	for i in range(m):
		index = ar[i]//b
		if cur==index:
			pass 
		else:
			ans += 1
			cur = index
	print(ans)