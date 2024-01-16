n = int(input())
val = n
l = []
num = 2

while n > 0:
    c = False
    for i in range(2, num):
        if num % i == 0:
            c = True
            break

    if not c:
        l.append(num)
        n -= 1

    num += 1

print(l[val-1])
