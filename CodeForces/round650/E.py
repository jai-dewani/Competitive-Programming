for _ in range(int(input())):
	# n = int(input())
	n, k = map(int, input().split())
	ar = list(input())
	letters = [0 for i in range(26)]
	for i in range(n):
		letters[ord(ar[i])-97] += 1
	print(letters)