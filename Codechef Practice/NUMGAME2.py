t = int(input())
for _ in range(t):
    n = int(input())
    if n%2==0:
        print('BOB')
    else:
        if n%4==1:
            print("ALICE")
        else:
            print("BOB")
