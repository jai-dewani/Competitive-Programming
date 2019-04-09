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
    for y in range(n):
        x,y = list(map(int,input().split()))
        if y == led[x]:
            print(0,7-len(leds[x]))
        elif y>led[x]:
            print('invalid')
        else:
            print(led[x]-y,led[x]-y+7-len(leds[x]))
