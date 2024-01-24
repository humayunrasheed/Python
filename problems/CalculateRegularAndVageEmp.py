class  Employee:
    def accept (self):
        self.name = input("Enter name: ")
        self.email = input("Enter email: ")
        self.code = input("Enter code: ")
        self.phone = input("Enter phone: ")
class RegularEmployee(Employee):
    def calculatePay(self, salary):
        self.salary = salary
        self.tax = self.salary * 0.1
        self.groseSalary = self.salary - self.tax
        return self.groseSalary // 12
    def display(self):
        print("Name:", self.name)
        print("Email:", self.email)
        print("Code:", self.code)
        print("Phone:", self.phone)
class WageEmployee(Employee):
    def calculatePay(self, wage):
        self.wage = wage
        self.net = self.wage * 30
        return self.net 
    def display(self):
        print("Name:", self.name)
        print("Email:", self.email)
        print("Code:", self.code)
        print("Phone:", self.phone)
        
    
print("Welcome to ABC corp Payroll System")
print("1. Regular Employee")
print("2. Wage Employee")
choice = int(input("Enter your choice: "))
# adding inheritance
if choice == 1:
    e = RegularEmployee()
    e.accept()
    salary = int(input("Enter salary: "))
    e.display()
    print("Pay of", e.name, "is", e.calculatePay(salary))
else:   
    e = WageEmployee()
    e.accept()  
    wage = int(input("Enter wage: "))
    e.display()
    print("Pay of", e.name, "is", e.calculatePay(wage))
