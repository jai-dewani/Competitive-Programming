for _ in range(int(input())):
    n,a,b,c = map(int,input().strip().split())
    ar = list(map(int,input().strip().split()))
    answer = 10**10
    for i in range(n):
        answer = min(answer,c+abs(b-ar[i])+abs(ar[i]-a))
    print(answer)