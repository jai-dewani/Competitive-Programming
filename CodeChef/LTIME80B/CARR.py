from random import randint
mod = 10**9+7

for _ in range(int(input())):
    n,m = map(int,input().strip().split())
    # n = randint(1,10**10)
    # m = randint(1,10**10)
    answer = 0
    fact = m*pow(m-1,n-1,mod)
    # for i in range(n-1):
    #     fact *= (m-1)
    answer += fact
    if(n>2):
        fact = m*pow(m-1,n-2,mod)
    elif n==2:
        fact = m
    # for i in range(n-2):
    #     fact *= (m-1)
    fact*= (n-1)
    fact %= mod
    answer += fact
    print(answer%mod)