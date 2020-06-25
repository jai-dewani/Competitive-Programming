def solve1():
	mini = 0
	maxi = n
	found =  False
	while mini!=maxi:
		print(10**9+1)
		a1 = input()
		while a1!='G':
			print(10**9+1)
			a1 = input()
		mid = (mini+maxi)//2
		print(mid)
		a1 = input()
		if a1=='E':
			found = True 
			break 
		elif a1=='L':
			maxi = mid - 1
		else:
			mini = mid + 1
	if not found:
		print(mini)
		a1 = input()

n = int(input())
solve1()
# mini = 0
# maxi = n 
# prev = '-1'
# found =  False
# while mini!=maxi:
# 	mid = (mini+maxi)//2
# 	print(mid)
# 	a1 = input()
# 	if a1=='E':
# 		found = True
# 		break
# 	if a1==prev:
# 		if a1=='G':
# 			mini = mid + 1
# 		else:
# 			maxi = mid - 1
# 		prev = '-1'
# 	else:
# 		prev = a1
# if not found:
# 	print(mini)
# 	a1 = input()
