t = int(input())
for z in range(t):
	n = int(input())
	ar = [0,0,0,0,0,0]
	for i in range(n):
		temp = input()
		ar[0] += temp.count('c')
		ar[1] += temp.count('d')
		ar[2] += temp.count('e')
		ar[3] += temp.count('f')
		ar[4] += temp.count('h')
		ar[5] += temp.count('o')
	ar[0] = ar[0]//2
	ar[2] = ar[2]//2
	print(min(ar))
