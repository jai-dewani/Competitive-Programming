t = int(input())
while t:
	n = int(input())
	temp = n//2
	ans = temp*temp+(n-temp)
	print(ans)
	t -= 1