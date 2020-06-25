for _ in range(int(input())):
	# n = int(input())
	n,x = map(int,input().split())
	ar = list(map(int,input().split()))
	sumi = sum(ar)
	if sumi%x==0:
		front = 0
		end = 0
		fl = 0
		el = 0
		for i in range(0,n):
			front += ar[i]
			fl += 1
			if front%x!=0:
				break 
		for i in range(n-1,-1,-1):
			end += ar[i]
			el += 1
			if end%x!=0:
				break 
		mini = min(fl,el)
		if mini==n:
			print(-1)
		else:
			print(n-mini)
	else:
		print(n)