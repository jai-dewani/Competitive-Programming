from collections import Counter
n = int(input())
ar = [int(x) for x in input().split()]

arr = [0 for i in range(11)]

more_than_zero = 0
unequal = 0
answer = 0
for i in range(len(ar)):
	if arr[ar[i]]==0:
		more_than_zero += 1
	arr[ar[i]] += 1
	dic = Counter(arr)
	dic.pop(0)

	count = list(dic.keys())
	
	if(len(count)==2 and (count[0]==1 or count[1]==1)):
		answer = i+1
		print("1",arr,dic,count)
		# unequal = 2
	elif(len(count)==1):
		answer = i+1
		print("2",arr,dic,count)
print(answer)