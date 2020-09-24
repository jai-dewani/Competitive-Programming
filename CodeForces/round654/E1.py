n,p = map(int,input().split())
ar = list(map(int,input().split()))
ar.sort()
ans = 0
m = max(ar)
l = m-n+1
for i in range(l,m):
	points = i
	inc = 0
	j = 0
	while j<n:
		while j<n:
			if ar[j]<=points:
				j += 1
			else:
				break 
		inc += 1
		if (j-inc)%p==0:
			break
	