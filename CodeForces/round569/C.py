n,q = list(map(int,input().split()))
ar = list(map(int,input().split()))
first_n = []
repeat = []
temp = [i for i in ar]
offset = 0
for i in range(n-1):
    first_n.append(temp[offset:offset+2])
    if temp[offset+0]>temp[offset+1]:
        temp.append(temp[offset+1])
        temp[1] = temp[offset+0]
    else:
        temp.append(temp[offset+0])
    offset+=1
#print(first_n)
for i in range(n-1):
    repeat.append(temp[offset:offset+2])
    if temp[offset]>temp[offset+1]:
        temp.append(temp[offset+1])
        temp[offset+1] = temp[offset]
    else:
        temp.append(temp[offset])
    offset+=1
#print(repeat)
for i in range(q):
    ques = int(input())
    if ques<n:
        print(*first_n[ques-1])
    else:
        ques = ques - n
        #print(ques)
        ques = ques%len(repeat)
        #print(ques)
        print(*repeat[ques])
