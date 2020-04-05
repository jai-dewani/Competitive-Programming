n,m = [int(x) for x in input().split()]
if m==0:
	print(1)
else:
	print(min(m,n-m))