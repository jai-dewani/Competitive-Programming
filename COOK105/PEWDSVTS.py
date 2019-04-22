import math
# [5, 9, 13, 15, 17, 19, 20, 21, 22]

def binarySearch(ar,key,low,high):
	mid = (low+high)//2
	# print(low,mid,high)
	if low>high:
		return low
	if ar[mid]==key:
		return mid
	elif ar[mid]>key:
		return binarySearch(ar,key,low,mid-1)
	else:
		return binarySearch(ar,key,mid+1,high)

def genrate(ar):
	temp = len(ar)
	for i in range(temp):
		j = ar[i]//2
		while j>0:
			ar.append(j)
			j = j//2
	# print(ar)
	ar.sort(reverse=True)
	# print(ar)
	summ = 0
	for i in range(len(ar)):
		summ += ar[i]
		ar[i] = summ
	# print(ar)


def modulo(a,b):
	temp = a%b
	if temp==0:
		return b
	else:
		return temp

def getDays(target,ar):
	ans = 0
	i = 0
	while target>0:
		target -= ar[i]
		i += 1
		ans += 1
	return ans

t = int(input())
for z in range(t):
	n,a,b,x,y,z = list(map(int,input().strip().split()))
	ar = list(map(int,input().strip().split()))

	hoolidays = math.ceil((z-b)/y)
	piperdays = math.ceil((z-a)/x)
	target = z-(hoolidays-1)*x-a
	sumar = sum(ar)

	if piperdays<hoolidays:
		print(0)

	elif piperdays == hoolidays:
		genrate(ar)
		target1 = modulo(z-a,x)

		if(sumar<target1):
			ans = binarySearch(ar,target,0,len(ar)-1)+1
			if(ans>len(ar)):
				print("RIP")
			else:
				print(ans)
		else:
			print("RIP")

	else:
		genrate(ar)
		if(sum(ar)<target):
			print("RIP")
		else:
			ans = binarySearch(ar,target,0,len(ar)-1)+1
			if(ans>len(ar)):
				print("RIP")
			else:
				print(ans)
	# print(target)