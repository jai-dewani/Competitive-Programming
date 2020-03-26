for _ in range(int(input())):
    n = int(input())
    answer = 0
    for i in range(n):
        s,p,v = map(int,input().strip().split())
        if (p//(s+1))*v>answer:
            answer = (p//(s+1))*v
    print(answer)