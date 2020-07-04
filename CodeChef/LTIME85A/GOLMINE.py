import heapq 
for _ in range(int(input())):
	n = int(input())
	ar = []
	for i in range(n):
		g,a,b = map(int,input().split())
		a_speed = g/a 
		b_speed = g/b 
		ar.append(g,a,a_speed,b,b_speed)
	heap_a = []
	heap_b = []
	for i in range(n):
		heap_a.append(ar[i][2])
		heap_b.append(a[i][4])
	