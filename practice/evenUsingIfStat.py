def even(num):
    if(num%2==0):
        return "even"
    elif(num%2!=0):
        return "odd"
num=int(input("Enter your number :"))
print("given number is",even(num))