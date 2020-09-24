n, m, k = map(int,input().split())
chips = []
for i in range(k):
    a = list(map(int,input().split()))
    chips.append(a)
targets = []
for i in range(k):
    a = list(map(int,input().split()))
    targets.append(a)
firstq = {}
secondq = {}
thirdq = {}
fourthq = {}
distances = []
for i in range(k):
    chip = chips[i]
    target = targets[i]
    distance = abs(chip[0]-target[0]) + abs(chip[1]-target[1])
    distance.append([i,distance,chip,target])
    if chip[0]>target[0] and chip[1]>target[1]:
        firstq[i] = [chip,target]
        
    elif chip[0]>target[0] and chip[1]<target[1]:
        secoundq[i] = [chip.target]

    elif chip[0]<target[0] and chip[1]<target[1]:
        thirdq[i] = [chip,target]

    else:
        fourthq[i] = [chip,target]
    
