print("Create account now")
name=input("Enter username: ")
password=input("Enter password: ")
print("Your account has been created successfully")
print("login now!")
name1=input("Enter username: ")
password2= input("Enter password: ")
if name1==name and password==password2:
    print("Logged in successfully")
else:
    print("Invalid credentials")