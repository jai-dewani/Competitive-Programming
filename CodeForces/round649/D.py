def dfs(node):
	dep = [-1 for i in range(n)]
	par = [-1 for i in range(n)]
	st = [(0,0)] 

n,m,k = map(int,input().split())
adj = {}
for i in range(n):
	adj[i] = []
for i in range(m):
	a,b = map(int,input().split())
	adj[i-1].append(j-1)
	adj[j-1].append(i-1)
dfs(0)
