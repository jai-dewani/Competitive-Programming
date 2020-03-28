from math import gcd
MOD = 10**9+7
def inverse(a, m=MOD) : 
    g = gcd(a, m) 
    if (g != 1) : 
        return -1          
    else :
        return power(a,m-2,m)
      
def power(x, y, m=MOD) :       
    if (y == 0) : 
        return 1
          
    p = power(x, y // 2, m) % m 
    p = (p * p) % m 
  
    if(y % 2 == 0) : 
        return p  
    else :  
        return ((x * p) % m)

nodes = [0]
for i in range(1,10**5+1):
    nodes.append(pow(2,i,MOD)*((i+1)//2))
#print(nodes[:10])
for i in range(1,10**5+1):
    nodes[i] = nodes[i-1] + nodes[i]
for i in range(int(input())):
    d = int(input())
    sumi = nodes[d]*2
    n = pow(2,d+1,MOD)-1
    total = (2*n*(n-1))%MOD
    inv = inverse(total)
    #print(sumi,total,inv)
    print(sumi*inv%MOD)
    
