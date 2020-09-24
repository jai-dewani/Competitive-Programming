for _ in range(int(input())):
	n = int(input())
	# n, x = map(int, input().split())
	ar = list(map(int, input().split()))
	ans = []
	maxi = max(ar)
	mini = min(ar)
	to_beat = maxi-mini 
	if ar[1]>ar[0]:
		direction = 'd'
	else:
		direction = 'u'
	ans.append(ar[0])
	for i in range(1,n):
		if direction=='u':
			if ar[i]>ans[-1]:
				ans[-1] = ar[i]
			elif ar[i]<ans[-1]:
				ans.append(ar[i])
				direction = 'd'
		else:
			if ar[i]<ans[-1]:
				ans[-1] = ar[i]
			elif ar[i]>ans[-1]:
				ans.append(ar[i])
				direction = 'u'
	print(len(ans))
	print(*ans)
	