import math 
hashmap = [-1,0,1,1,0,1,0,1,0,1,0]
two = set()
for i in range(33):
	two.add(2**i)
for _ in range(int(input())):
	n = int(input())
	# n,m = map(int,input().split())
	# ar = list(map(int,input().split()))
	if n<10:
		if hashmap[n]==1:
			print("Ashishgup")
		else:
			print("FastestFinger")
	else:
		prime = True 
		ans = False 
		if n in two: 
			ans = True
		elif n%2==0:
			n = n//2 
		else:
			prime = False 
		if prime==True and ans==False:
			for i in range(2,int(math.sqrt(n)+2)):
				if n%i==0:
					prime = False 
					break 
		if prime:
			print("FastestFinger")
		else:
			print("Ashishgup")
		
