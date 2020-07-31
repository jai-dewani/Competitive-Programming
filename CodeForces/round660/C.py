from queue import Queue
class Node:
    def __init__(self,val):
        super().__init__()
        self.val = val
        self.nodes = []
        self.people_pass = 0
        self.pop = None 

for _ in range(int(input())):
    n,m = map(int,input().split())
    people = list(map(int,input().split()))
    happy = list(map(int,input().split()))
    parent = [-1]*n
    nodes = [Node(i) for i in range(n)]
    negative = [0]*n
    for i in range(n):
        nodes[i].pop = people[i]

    for i in range(n-1):
        x,y = map(int,input().split())
        nodes[x-1].nodes.append(y-1)
        nodes[y-1].nodes.append(x-1)
    q = Queue()
    q.put(0)
    while not q.empty():
        no = q.get()
        for i in nodes[no].nodes:
            if parent[i]==-1:
                parent[i] = no 
                q.put(i)
    parent[0] = -1
    assert parent[0]==-1
    for i in range(n):
        node = i
        pop = people[i]
        while node!=0:
            nodes[node].people_pass += pop 
            node = parent[node]
    for i in nodes[0].nodes:
        nodes[0].people_pass += nodes[i].people_pass
    nodes[0].people_pass += people[0]
    # print([nodes[i].people_pass for i in range(n)])
    # print(happy)

    flag = True
    for i in range(n):
        temp = nodes[i].people_pass 
        if temp>=happy[i]>=(-1*temp) and happy[i]%2==temp%2:
            pass
        else:
            flag = False
            # print(i)

    if flag:
        for i in range(n):
            negative[i] = (nodes[i].people_pass - happy[i])//2
        getN = [0]*n
        for i in range(1,n):
            node = i
            neg = negative[i]
            if len(nodes[i].nodes)==1:
                getN[i] = neg
            node = parent[node]
            getN[node] += neg

        # print(negative)
        # print(getN)

        for i in range(n):
            if negative[i]>getN[i]+nodes[i].pop:
                flag = False
        if flag:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")