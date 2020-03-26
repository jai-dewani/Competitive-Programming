t = int(input())
while t:
	n = int(input())
	temp = n//2
	ans = temp*temp+(n-temp)
	print(ans%(10**9+7))
	t -= 1