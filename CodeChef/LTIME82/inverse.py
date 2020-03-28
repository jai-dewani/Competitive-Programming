from math import gcd
def inverse(a, m) : 
    g = gcd(a, m) 
    if (g != 1) : 
        return -1          
    else :
        return power(a,m-2,m)
      
def power(x, y, m) :       
    if (y == 0) : 
        return 1
          
    p = power(x, y // 2, m) % m 
    p = (p * p) % m 
  
    if(y % 2 == 0) : 
        return p  
    else :  
        return ((x * p) % m)       

a = 3; m = 11
a = int(input())
m = 10**9+7
b = modInverse(a, m)
print(b)
