class voter_id:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def disp(self):
        print(self.name)
        v1 = validate()
        v1.validate(self.age)
    
class driving_lisence:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def disp(self):
        print(self.name)
        v2 = validate()
        v2.validate(self.age)

class validate:
    def validate(self, age):
        self.age = age
        if self.age >= 18:
            print("Eligible")
        else:
            print("Not Eligible")

choice = int(input())
name = input()
age = int(input())
if choice == 1:
    obj1 = voter_id(name,age)
    obj1.disp()
elif choice == 2:
    obj2 = driving_lisence(name,age)
    obj2.disp()
else:
    print("Invalid Choice")