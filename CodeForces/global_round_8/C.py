from queue import Queue
n = int(input())
center = [500,500]
if n==1:
	print(7)
	nodes = [[2,2],[1,2],[3,2],[2,3],[2,1],[1,1],[3,3]]
	for i in nodes:
		print(*i)
elif n%2==0:
	start = [1,3]
	nodes = []
	pattern = [[2,3],[3,3],[4,3],[5,3],[3,2],[4,2],[3,4],[4,4]]
	step = 4
	for i in range(n//2):
		shift = step*i 
		for j in pattern:
			nodes.append([j[0]+shift, j[1]])
	end = [2+4*(n//2),3]			
	nodes.append([start[0],start[1]])
	nodes.append([end[0],end[1]])
	for i in range(1,4):
		start[1] += 1
		end[1] += 1
		nodes.append([start[0],start[1]])
		nodes.append([end[0],end[1]])
	while start[0]!=end[0]:
		start[0] += 1
		nodes.append([start[0],start[1]])
	nodes.pop()
	print(len(nodes))
	for i in nodes:
		print(*i)
else:
	start = [1,3]
	nodes = []
	pattern = [[2,3],[3,3],[4,3],[5,3],[3,2],[4,2],[3,4],[4,4]]
	step = 4
	for i in range(n//2):
		shift = step*i 
		for j in pattern:
			nodes.append([j[0]+shift, j[1]])
	end = [2+4*(n//2),3]			
	single = [[0,0],[2,0],[2,-1],[1,-1]]
	for j in single:
		nodes.append([end[0]+j[0], end[1]+j[1]])
	end = [end[0]+1,end[1]]
	nodes.append([start[0],start[1]])
	nodes.append([end[0],end[1]])
	for i in range(1,4):
		start[1] += 1
		end[1] += 1
		nodes.append([start[0],start[1]])
		nodes.append([end[0],end[1]])
	
	while start[0]!=end[0]:
		start[0] += 1
		nodes.append([start[0],start[1]])
	nodes.pop()
	print(len(nodes))
	for i in nodes:
		print(*i)