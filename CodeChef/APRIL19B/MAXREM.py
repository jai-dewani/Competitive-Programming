n = int(input())
ar = list(map(int,input().split()))
ar = list(set(ar))
ar.sort()
try:
	print(ar[-2])
except:
	print(0)