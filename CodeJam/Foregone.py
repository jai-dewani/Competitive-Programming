t = int(input())
for z in range(t):
    n = list(input())
    ans1 = '' 
    for i in n:
        if i=='4':
            ans1+='2'
        else:
            ans1+=i
    
    ans2 = ''
    for a in n:
        if a=='4':
            ans2 +='2'
        else:
            ans2+='0'
    print('Case #'+str(z+1)+': '+str(int(ans1)),str(int(ans2)))