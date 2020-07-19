class Node:
    def __init__(self,val):
        self.val = val 
        self.nodes = []
from queue import Queue

prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97,103]
dep = []
cost = 2*3*5*7*11*13*17*19*23*31
for i in range(30):
    dep.append(cost)
j = 11
for i in range(30,101):
    if prime[j+1]==i:
        j += 1
    dep.append(cost*prime[j])

for _ in range(int(input())):
    n = int(input())
    nodes = [Node(i+1) for i in range(n)]
    for i in range(n-1):
        u,v = map(int,input().split())
        u,v = u-1,v-1 
        nodes[u].nodes.append(v)
        nodes[v].nodes.append(u)
    root = None
    depth = 0 
    q = Queue()
    q.put((0,0))
    visited = [0]*n
    visited[0] = 1
    while not q.empty():
        a,d = q.get()
        if d>depth:
            root = a 
            depth = d 
        for node in nodes[a].nodes:
            if visited[node]==0:
                visited[node]=1
                q.put((node,d+1))
    A = [-1]*n 
    q = Queue()
    q.put((root,0))
    visited = [0]*n 
    visited[root] = 1
    while not q.empty():
        a,d = q.get()
        A[a] = dep[d]
        for node in nodes[a].nodes:
            if visited[node]==0:
                visited[node]=1
                q.put((node,d+1))
    for i in range(n):
        print(i,A[i])
