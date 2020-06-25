import math
for _ in range(int(input())):
	# n = int(input())
	n,k = map(int,input().split())
	ar = list(input())
	ones = []
	for i in range(n):
		if ar[i]=='1':
			ones.append(i)
	if len(ones)==0:
		ans = math.ceil(n/(k+1))
	else:
		ans = 0 
		ans += ones[0]//(k+1)
		ans += (n-ones[-1]-1)//(k+1)
		# print(ones,ans)
		for i in range(1,len(ones)):
			ans += (ones[i] - ones[i-1]-1-k)//(k+1)
	print(ans)
