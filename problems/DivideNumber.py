#try catch using in python

def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return "You are dividing by zero"
    except TypeError:
        return "You are dividing by a non number"
    except :
        return "Unknown error"
    finally:
        print("Executed")
a = int(input("Enter a: "))
b = int(input("Enter b:"))
print(divide(a,b))