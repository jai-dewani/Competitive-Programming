n = int(input())
sqrt = int(pow(n,0.5))
ar = [1]
for i in range(2,sqrt+1):
	if n%i==0:
		ar.append(i)
		ar.append(n//i)
# print(ar)
if n==1:
	print("Not Perfect")
elif sum(ar)==n:
	print("Perfect")
else:
	print("Not Perfect")