for _ in range(int(input())):
	# n = int(input())
	a,b,n = map(int, input().split())
	# ar = list(map(int, input().split()))
	count = 0
	if b>a:
		a,b = b,a 
	while a<=n:
		b += a 
		a,b = b,a 
		count += 1
	print(count)