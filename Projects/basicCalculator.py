i =0
def cal(a,b,op):

    if op=="+":
      print("addition is ",a+b)
    elif op =="-":
      print("subtraction is ",a-b)
    elif op=="/":
      print("division is ",a/b)
    elif op=="*":
        print("multiplication is ",a*b)
    elif op=="%":
        print("reminder is ",a%b)
    else:   
       print("Invalid operator")
    
while i==0:
    a=int(input("Enter the first number :"))
    b=int(input("Enter the second number :"))
    op= input("Enter the operator :")
    cal(a,b,op)
    i=int(input("Enter 0 to continue and 1 to exit :"))