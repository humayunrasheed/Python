sum = 0
n = int(input())
while(n>0 or sum >9):
    if(n==0):
        n = sum
        sum = 0
    rem = n %10
    sum = sum + rem
    n= n//10
print(sum)