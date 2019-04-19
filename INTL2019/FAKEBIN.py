t = int(input())
while t:
	n = int(input())
	ar = list(map(int,input().strip().split()))
	print(sum(ar))
	t -= 1	