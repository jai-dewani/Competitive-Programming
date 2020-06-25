for _ in range(int(input())):
	n = int(input())
	# n,m = map(int,input().split())
	ar = list(map(int,input().split()))
	odd = []
	even = []
	for i in range(n):
		if i%2==ar[i]%2:
			pass
		else:
			if i%2:
				odd.append(i)
			else:
				even.append(i)
	if len(odd)==len(even):
		print(len(odd))
	else:
		print(-1)