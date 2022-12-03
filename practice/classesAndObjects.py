class Person:
    def __init__(self,name,age):
        self.name= name
        self.age=age

p1=Person('humayun',20)
print(p1.name)
print(p1.age)
name=input("Enter your name :")
age= input("Enter your age :")
p2=Person(name,age)
print(p2.name)
del p1 # delete the class p1