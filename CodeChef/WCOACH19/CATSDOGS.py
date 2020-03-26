t = int(input())
for z in range(t):
	c,d,l = list(map(int,input().split()))
	temp = max(c-2*d,0)
	if (c+d)*4<l:
		print("no")
	elif (temp+d)*4>l:
		print("no")
	elif l%4!=0:
		print("no")
	else:
		print("yes")