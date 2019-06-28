t = int(input())
for _ in range(t):
    n = int(input())
    correct = input()
    answer = input()
    i = 0
    points = 0
    while i<n:
        if correct[i]==answer[i]:
            points += 1
        elif answer[i]!='N':
            i +=1
        i+=1
    print(points)
