def dectobase(number):
    ar = list(str(number))
    #print(ar)
    base = ord(max(ar))-55+1
    #print(base)
    ans = 0
    value = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
             'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15, 'G': 16, 'H': 17, 'I': 18,
             'J': 19, 'K': 20, 'L': 21, 'M': 22, 'N': 23, 'O': 24, 'P': 25, 'Q': 26, 'R': 27,
             'S': 28, 'T': 29, 'U': 30, 'V': 31, 'W': 32, 'X': 33, 'Y': 34, 'Z': 35}
    l = len(ar)
    #print(l)
    for i in range(len(ar)):
        #print(value[ar[l-i-1]])
        ans += value[ar[l-i-1]]*(base**i)
    return ans
    

def int2roman(number):
     numerals={1:"I", 4:"IV", 5:"V", 9: "IX", 10:"X", 40:"XL", 50:"L",
               90:"XC", 100:"C", 400:"CD", 500:"D", 900:"CM", 1000:"M"}
     result=""
     for value, numeral in sorted(numerals.items(), reverse=True):
         while number >= value:
             result += numeral
             number -= value
     return result

n = int(input())
ar = [0 for i in range(3999)]
while n<=3999:
    ar = [-1 for i in range(3999)]
    result = int2roman(n)
    #print(result)
    n = dectobase(result)
    #print(n)
    
print(n)
