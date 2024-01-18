a,b= map(int,input("Enter a and b:").split())
op= input("Enter operator +,-,*,/,//,%,** :")
if (op == "+"):
    print(a+b)
elif(op=='-'):
    print(a-b)
elif(op=='*'):
    print(a*b)
elif(op=='/'):
    print(a/b)
elif(op=='//'):
    print(a//b)
elif(op=='%'):
    print(a%b)
elif(op=="**"):
    print(a**b)
else:
    print("Invalid operator")