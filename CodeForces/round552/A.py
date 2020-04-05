ar = list(map(int,input().strip().split()))
ans = max(ar)
for i in range(len(ar)):
	ar[i] = ans -ar[i]
ar.sort(reverse=True)
print(ar[0],ar[1],ar[2])