a,b,c = [int(x) for x in input().split()]
ar = [a//3,b//2,c//2]
weeks = min(ar)
left = [a-3*weeks,b-2*weeks,c-2*weeks]
week = [0,1,2,0,2,1,0]
# print(left)
ans =  0
for i in range(7):
	hi = 0
	temp = left[:]
	# print(temp,left)
	while temp[week[(i+hi)%7]]>0:
		temp[week[(i+hi)%7]] -= 1
		hi += 1
		# print(temp,left)
	ans = max(ans,hi)
# print(ans)
# print(weeks*7)
print(weeks*7+ans)