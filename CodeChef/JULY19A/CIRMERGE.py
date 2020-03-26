from random import randint

class Node:
    def __init__(self,value,prev_node=None):
        self.value = value
        self.next = None
        self.prev = prev_node

def brute(ar,cost):
    n = len(ar)
    if n==1:
        return cost
    else:
        back = []
        #print(ar,cost)
        for i in range(0,len(ar)-1):
            temp_cost = cost
            temp = [ar[j] for j in range(0,i)]
            temp.append(ar[i]+ar[(i+1)%n])
            for j in range(i+2,n):
                temp.append(ar[j])
            temp_cost += ar[i]+ar[i+1]
            #print(i,"IN",ar,temp,temp_cost)
            back.append(brute(temp,temp_cost))
        temp = [ar[j] for j in range(1,len(ar)-1)]
        temp.append(ar[0]+ar[-1])
        temp_cost = cost
        temp_cost += ar[0]+ar[-1]
        back.append(brute(temp,temp_cost))
        #print(back)
        return min(back)

def op(ar):
    n = len(ar)
    start = Node(ar[0])
    temp = start
    prev = start
    for i in range(1,len(ar)):
        temp.next = Node(ar[i],temp)
        temp = temp.next
    start.prev = temp
    temp.next = start
    
    cost = 0
    for i in range(n-1):
        temp = start
        mini = ar[0]+ar[1]
        min_sum = None
        for j in range(n-i):
            if mini>temp.value+temp.next.value:
                mini_sum = temp
                mini = temp.value+temp.next.value
        cost += mini
        prev = temp.prev
        prev.next = Node(mini,prev)
        prev.next.next = temp.next.next
    return cost

def try1(ar):
    cost = 0
    n = len(ar)
    for i in range(n-1):
        print(ar,cost)
        min_sum = ar[0]+ar[1]
        min_index = 0
        for j in range(len(ar)):
            if min_sum>ar[j]+ar[(j+1)%len(ar)]:
                min_sum = ar[j]+ar[(j+1)%len(ar)]
                min_index = j
        ar.pop(min_index)
        ar.pop(min_index%len(ar))
        print('removed',ar,min_sum)
        ar.insert(min_index,min_sum)
        cost += min_sum
    return cost

t = int(input()) 
for _ in range(t):
    n = int(input())
    #n = randint(1,10)
    ar = list(map(int,input().strip().split()))
    '''
    ar = []
    for i in range(n):
        ar.append(randint(1,50))
    '''
    copy = [i for i in ar]
    print("brute....")
    ans1 = brute(ar,0)
    print("short....")
    ans2 = try1(ar)
    if ans1!=ans2:
        print("ERROR",copy,ans1,ans2)
        break
    print(copy,ans1,ans2)
