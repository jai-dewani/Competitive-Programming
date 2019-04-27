t = int(input())
while t:
	n = int(input())
	array = []
	names = {}
	for _ in range(n):
		first,last = input().split()
		array.append([first,last])
		if first in names:
			names[first]  += 1
		else:
			names[first] = 1
	for ar in array:
		if names[ar[0]]==1:
			print(ar[0])
		else:
			print(ar[0],ar[1])
	t -= 1