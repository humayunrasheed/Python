sum = 0
c = 1
n = int(input())
while(n>0):
    r = n %10
    if r % 2 == 0:
        sum +=(r + 1)*c
    else :
        sum += (r -1) * c
    c = c *10
    n = n // 10
print(sum)