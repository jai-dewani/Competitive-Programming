class Node:
    def __init__(self):
        self.value = None
        self.nodes = []

n, m = map(int,input().split())
nodes = []
topics = {}
for i in range(n):
    nodes.append(Node())
for i in range(m):
    a,b = map(int,input().split())
    nodes[a-1].nodes.append(b-1)
    nodes[b-1].nodes.append(a-1)
ar = list(map(int,input().split()))
for i in range(n):
    topic = ar[i]
    nodes[i].value = topic
    if topics.get(topic)==None:
        topics[topic] = [i]
    else:
        topics[topic].append(i)
possible = True
order = []
for i in sorted(topics.keys()):
    t = topics[i]
    for j in t:
        seet = set()
        for node in nodes[j].nodes:
            if nodes[node].value==i:
                possible=False
                break
            if nodes[node].value<i:
                seet.add(nodes[node].value)
        else:
            if len(seet)==i-1:
                order.append(j+1)
            else:
                possible = False
                break
    if possible==False:
        break
if possible:
    print(*order)
else:
    print(-1)