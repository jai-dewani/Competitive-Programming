led = [6,2,5,5,4,5,6,3,7,6]
leds = [
    {0,1,2,3,4,5},
    {2,3},
    {1,2,4,5,6},
    {1,2,3,4,6},
    {0,2,3,6},
    {0,1,3,4,6},
    {0,1,3,4,5,6},
    {1,2,3},
    {0,1,2,3,4,5,6},
    {0,1,2,3,4,6}
    ]

t = int(input())
for z in range(t):
    n = int(input())
    right = []
    wrong = []
    currentLeds = {}
    flag = False
    for y in range(n):
        x,y = list(map(int,input().split()))
        if led[x]==y:
            right.append(x)
            currentLeds = currentLeds.union(leds[x])
        elif y>led[x]:
            flag = True
            break
        else:
            if leds[x].issubset(currentLeds):
                flag = True
                break
            wrong.append(x)
    if !flag:
        for i in range(len(wrong)):
            if leds[wrong[i]].issubset(currentLeds):
                flag = True
                break
    if flag:
        print('invalid')
    else:
        
    
