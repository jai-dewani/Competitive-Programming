for _ in range(int(input())):
	# n = int(input())
	n,m = map(int,input().split())
	ar = list(map(int,input().split()))
	hashmap = [0 for i in range(m+1)]
	ans = True 
	cou = 0
	for i in range(n):
		if ar[i]<m and hashmap[ar[i]]==0:
			cou += 1
		if ar[i]<=m:
			hashmap[ar[i]] += 1
	# print(cou)
	if cou==m-1:
		if hashmap[m]>0:
			print(n-hashmap[m])
		else:
			print(n)
	else:
		print(-1)