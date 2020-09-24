for _ in range(int(input())):
	n = int(input())
	# n,m = map(int,input().split())
	ar = list(map(int,input().split()))
	odd = []
	even = []
	for i in range(2*n):
		if ar[i]%2:
			odd.append(i+1)
		else:
			even.append(i+1)
	# print(odd,even)
	if len(odd)>0:
		if len(odd)%2==0:
			odd.pop()
			odd.pop()
		else:
			odd.pop()
			even.pop()
	else:
			even.pop()
			even.pop()

	# print(odd,even)
	while len(odd)>0:
		# print(odd)
		a = odd.pop()
		b = odd.pop()
		print(a,b)
	while len(even)>0:
		# print(even)
		a = even.pop()
		b = even.pop()
		print(a,b)