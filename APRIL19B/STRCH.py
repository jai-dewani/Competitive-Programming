t = int(input())
for z in range(t):
	n = int(input())
	s,x = input().split()
	ar = [-1]
	for i in range(len(s)):
		if x==s[i]:
			ar.append(i)
	ar.append(len(s))

	ans = 0
	# print(ar)
	for i in range(1,len(ar)-1):
		temp = ((ar[i]-ar[i-1])*(len(s)-ar[i]))
		# print(temp)
		ans += temp
	print(ans)
	# ans = 0
	# length = len(s)
	# # print(ar)
	# for i in range(len(s)):
	# 	maxx = i
	# 	for j in ar:
	# 		if j>=maxx:
	# 			maxx = j
	# 			break
	# 	# print(i,maxx)
	# 	ans += length - maxx
	# print(ans)