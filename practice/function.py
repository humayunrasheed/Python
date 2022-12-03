def greetings_functions(name,age):
    print("Welcome " +name+ ". you are "+age+ " old.")
    
name=input("Enter your name :")
age=input("Enter your age :")
greetings_functions(name,age)
    
def greetings_functions2(*names):
    print("Welcome",names[2])
names=("Tom","Humayun","Rasheed")
greetings_functions2(*names)