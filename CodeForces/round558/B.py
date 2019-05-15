from collections import Counter

n = int(input())
ar = [int(x) for x in input().split()]
hash = [0 for i in range(11)]
temp_ar = []
answer = 0
for i in range(n):
    hash[ar[i]] += 1
    dic = Counter(hash)
    dic.pop(0)
    keys = list(dic.keys())
    values = list(dic.values())
    
    if len(keys)==2:
        if values[0]==1 or values[1]==1:
            if values[0]==1 and keys[0]==1:
                answer = i+1
                print(i,hash,dic,keys,values)
            elif values[1]==1 and keys[1]==1:
                answer = i+1
                print(i,hash,dic,keys,values)
        
        if keys[0]-keys[1]==1 and values[0]==1:
            answer = i+1
            print("5",i,hash,dic,keys,values)
        elif keys[1]-key[0]==1 and values[1]==1:
            answer = i+1
        '''
        if temp_ar[0]==1 or temp_ar[1]==1:
            answer = i+1
        elif (temp_ar[0]-temp_ar[1])==1:
            answer = i+1
        ''' 
    elif len(keys)==1 and keys[0]==1:
        answer = i+1
        
print(answer)
