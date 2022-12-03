boy=True
short=True
if boy is True:
    if short is True:
        print("he is a boy and he is short")
    else:
        print("he is a boy but he is not short")
else:
    print("he is not a boy")
value=int(input("enter a value: "))
if type(value)== str:
    print(value," is a string")
else:
    print(value, " is an integer")
if value<10:
    print(value,"is less then 10")
elif value==10:
    print(value, " is equal to 10")
else:
    print(value ," is greater then 10")