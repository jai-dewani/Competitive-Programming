for _ in range(int(input())):
	n,k = map(int,input().split())
	ans = [[0 for i in range(n)] for j in range(n)]
	i = 0 
	j = 0
	while i<k:
		x = 0 
		y = j 
		while x<n and i<k:
			ans[x][y] = 1 
			i += 1 
			x += 1 
			y = (y+1)%n
		j += 1
	if k%n==0:
		print(0)
	else:
		print(2)
	for j in ans:
		print(''.join(str(x) for x in j))