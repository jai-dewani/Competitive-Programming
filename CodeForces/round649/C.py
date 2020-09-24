from heapq import heappush, heappop
n = int(input())
ar = list(map(int, input().split()))

valid = True
s = []
for i in range(n):
	if ar[i]>i+1:
		valid = False 
		break 
	else:
		if i>0:
			for j in range(ar[i-1]+1,ar[i]):
				heappush(s,j)
		elif ar[0]==1:
			heappush(s,0)
		# print(i,s)
if not valid:
	print(-1)
else:
	maxi = ar[-1]+1
	s_len = len(s)
	for i in range(s_len,n):
		heappush(s,maxi)
		maxi += 1
	# print(s)
	ans = []
	for i in range(n):
		k = heappop(s)
		ans.append(k)
		# s.remove(k)
		if i+1<n and ar[i]!=ar[i+1]:
			heappush(s,ar[i])
	print(*ans)