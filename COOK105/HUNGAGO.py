t = int(input())
for z in range(t):
	n = int(input())
	ar = []
	col = [0 for i in range(n)]
	row = [0 for i in range(n)]
	for i in range(n):
		ar.append(list(map(int,input().strip().split())))
		for j in range(len(ar[i])):
			if ar[i][j]==0:
				row[i] = 1
				col[j] = 1
	# print(*row)
	# print(*col)
	flag = True
	for i in col:
		if i==0:
			flag = False
			break
	if flag:
		for i in row:
			if i==0:
				flag = False
				break
	if flag:
		print("YES")
	else:
		print("NO")