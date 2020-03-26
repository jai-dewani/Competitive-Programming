def modInverse(a, m) : 
	  
	g = gcd(a, m) 
	  
	if (g != 1) : 
		print("Inverse doesn't exist") 
		  
	else : 
		  
		# If a and m are relatively prime, 
		# then modulo inverse is a^(m-2) mode m 
		ans = power(a,m-2,m)
		return ans
	  
# To compute x^y under modulo m 
def power(x, y, m) : 
	  
	if (y == 0) : 
		return 1
		  
	p = power(x, y // 2, m) % m 
	p = (p * p) % m 
  
	if(y % 2 == 0) : 
		return p  
	else :  
		return ((x * p) % m) 
  
# Function to return gcd of a and b 
def gcd(a, b) : 
	if (a == 0) : 
		return b 
		  
	return gcd(b % a, a) 
a = 15
m = 10**9+7
b = modInverse(a,m)
print((4*b)%m)
for i in range(1,1000):
	for j in range(1,1000):
		b = (modInverse(j,m)*i)%m
		if b==866666673:
			print(i,j)