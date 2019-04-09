t = int(input())
for z in range(t):
	n = int(input())
	s = list(input())
	ans = ''
	for i in s:
		if i=='S':
			ans += 'E'
		else:
			ans += 'S'
	print('Case #'+str(z+1)+': '+ans)