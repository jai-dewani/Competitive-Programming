N = 5*10**5
for _ in range(int(input())):
	# n = int(input())
	n,c = map(int,input().split())
	ar = []
	for i in range(n):
		ar.append(list(map(int,input().split())))
	group = {}
	moves = 0

	for i in range(-N,N+1):
		group[i] = []
	for i in range(n):
		gr = ar[i][0]-ar[i][1]
		if group[gr]==[]:
			group[gr].append(ar[i])
		else:
			for j in group[gr]:
				if (j[0]-ar[i][0])%c==0:
					moves = abs(j[0]-ar[i][0])//c
					break 
			else:
				group[gr].append(ar[i])
	cp = sum([len(group[i]) for i in group.keys()])
	print(cp,moves)