n = int(input())
def getSum(n): 
    
    sum = 0
    for digit in str(n):  
      sum += int(digit)       
    return sum
while(n>26):
    n = getSum(n)
print(chr(96+n))