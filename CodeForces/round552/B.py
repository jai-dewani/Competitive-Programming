n = int(input())
ar = list(map(int,input().strip().split()))
arset = list(set(ar))
arset.sort()
if len(arset)<3:
	if len(arset)==1:
		print(0)
	else:
		if (arset[0]-arset[1])%2==0:
			print(abs(arset[0]-arset[1])//2)
		else:
			print(abs(arset[0]-arset[1]))
elif len(arset)==3:
	# print(arset)
	if arset[0]+arset[2]==2*arset[1]:
		print(abs(arset[2]-arset[1]))
	else:
		print(-1)
else:
	print(-1)