class Applicant:
    name = ""
    city = ""
    count = 0
    def __init__(self, name, city):
        self.name = name
        self.city = city
        Applicant.count += 1
    def display(self):
        print("Name:", self.name)
        print("City:", self.city)

a1 = Applicant("Ravi", "Pune")
a2 = Applicant("Priya", "Mumbai")
a3 = Applicant("Rahul", "Delhi")
print("Total Applicants:", Applicant.count)