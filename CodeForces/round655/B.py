from math import sqrt
for _ in range(int(input())):
	n = int(input())
	# n,m = map(int,input().split())
	# ar = list(map(int,input().split()))
	if n//2==0:
		x,y = n//2,n//2
	else:
		for i in range(2,int(sqrt(n))+2):
			if n%i==0:
				x = n//i
				y = n-x 
				break 
		else:
			x = n-1
			y = 1 
	print(x,y)