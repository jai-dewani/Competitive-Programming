hashmap = [0]*(2*10**6+1)
MOD = 10**9+7
a,b = 1,1
claw = 0 
for i in range(2,2*10*6+1):
    hashmap[i] = claw 
    claw += a 
    claw %= MOD
    a,b = b, a*2+b
    a,b = a%MOD, b%MOD

for _ in range(int(input())):
    n = int(input())
    print(hashmap[n])
    # s = input()
    # n,m = map(int,input().split())
    # ar = list(map(int,input().split()))