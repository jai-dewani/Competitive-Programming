char = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

t = int(input())
for z in range(t):
	n,l = list(map(int,input().split()))
	ar = list(map(int,input().split()))
	primes = []
	for i in range(2,int(pow(ar[0],0.5))+2):
		if ar[0]%i==0:
			primes.append(i)
			break
	for i in ar:
		primes.append(i//primes[-1])
	ar = list(set(primes))
	ar.sort()
	print(len(ar))
	# print(ar)
	# print(primes)
	dic = {ar[i]:char[i] for i in range(26)}
	print(dic)
	ans = ''
	for i in primes:
		ans += dic[i]
	print('Case #'+str(z+1)+': '+ans)