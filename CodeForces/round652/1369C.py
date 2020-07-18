for _ in range(int(input())):
    n,k = map(int,input().split())
    integers = list(map(int,input().split()))
    give = list(map(int,input().split()))
    integers.sort()
    give.sort(reverse=True)
    ones = 0
    for i in give:
        if i==1:
            ones += 1 
    start = 0
    end = n-1 
    happy = 0
    for i in range(ones):
        happy += 2*integers[end]
        end -= 1
    for i in range(k-ones):
        happy += integers[end] + integers[start]
        start += give[i]-1
        end -= 1
    print(happy)
