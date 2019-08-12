rr1 = float(input())
batsmen = list(map(int,input().strip().split()))
runs = input().strip().split() 
rr2 = float(input())
b2 = len(runs)
r2 = 0

for i in range(b2):
    if runs[i]!='W':
        r2+=int(runs[i])
over = ((rr2*b2/6)-r2)/(rr1-rr2)
b1 = round(over*6)
r1 = round(b1*rr1/6)
#print(b1,r1+r2)

strike = 0
balls_left = 6-b1%6
for i in range(b2):
    
    if runs[i] == 'W':
        batsmen[strike] = 0
    else:
        run = int(runs[i])
        if run == 1 or run == 3 or run == 5:
            batsmen[strike] += run
            strike = 1 - strike
        else:
            batsmen[strike] += run
        print(i,run,batsmen)
    balls_left -= 1            
    if balls_left == 0:
        strike = 1 - strike
        balls_left = 6
print(str(r1+r2)+' ' +str(batsmen[strike])+' '+str(batsmen[1-strike]),end='')
