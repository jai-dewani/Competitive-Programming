t = int(input())
for z in range(t):
	n = list(input())
	temp = 0
	flag = True
	for i in n:
		if i=='/':
			temp += 1
		else:
			temp -= 1
		if temp<0:
			flag = False
			break
	if flag:
		print("Regular since Childhood.")
	else:
		print("Irregular since Childhood.")