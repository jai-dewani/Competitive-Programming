for _ in range(int(input())):
	# n = int(input())
	# n,m = map(int,input().split())
	# ar = list(map(int,input().split()))
	s = input()
	ans = ""
	ans = s[0]
	for i in range(1,len(s),2):
		ans += s[i]
	# ans += s[-1]
	print(ans)