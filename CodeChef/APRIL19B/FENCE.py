t = int(input())
for z in range(t):
	n,m,k = list(map(int,input().strip().split()))
	array = {}
	for i in range(k):
		n,m = list(map(int,input().strip().split()))
		try:
			array[n].append(m)
		except:
			array[n] = [m]
	for i in array:
		array[i].sort()

	# print(array)
	ans = 0
	for i in array:
		for j in array[i]:
			temp = 0
			if j+1 in array[i]:
				temp += 1
			if j-1 in array[i]:
				temp += 1
			try:
				if j in array[i+1]:
					temp += 1
			except:
				pass
			try:
				if j in array[i-1]:
					temp += 1
			except:
				pass
			ans += 4-temp

	print(ans)