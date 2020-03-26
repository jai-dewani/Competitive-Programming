class City:
    def __init__(self,index):
        self.val = index
        self.connected = []

def dfs(city,count,roads):
    count += 1
    # print(city.val,count)
    if not visited[city.val]:
        roads += len(city.connected)
    visited[city.val] = True
    for i in city.connected:
        if not visited[i.val]:    
            count,roads = dfs(i,count,roads)
    return (count,roads)

n,m = map(int,input().strip().split())
visited = [False]*n
cities = [City(i) for i in range(n)]
for i in range(m):
    u,v = map(int,input().strip().split())
    v -= 1
    u -= 1
    cities[u].connected.append(cities[v])
    cities[v].connected.append(cities[u])
states = []

for i in range(n):
    if visited[i]==False:
        count,roads = dfs(cities[i],0,0)
        states.append([count,roads//2])
        # print('-----------')
# print(states)
presentRoads = 0
roadsNeeded = 0
for i in range(len(states)):
    presentRoads += states[i][1]
    temp = states[i][0]
    roadsNeeded += (temp*(temp-1))//2
print(roadsNeeded-presentRoads,end='')