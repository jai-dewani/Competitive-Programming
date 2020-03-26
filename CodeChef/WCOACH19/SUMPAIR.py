t = int(input())
for z in range(t):
	n,d = list(map(int,input().split()))
	ar = list(map(int,input().split()))
	ar.sort()
	ans = 0
	i = n-1
	while i>0 and len(ar)>0:
		if ar[i]-ar[i-1]<d:
			ans += ar[i]+ar[i-1]
			ar.pop(i)
			ar.pop(i-1)
			i -= 1
		i -= 1

	print(ans)