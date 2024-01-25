#add variabel list of student id 
# implementing using functions
def linear_search(student_id, id_to_search):
    for i in range(len(student_id)):
        if student_id[i] == id_to_search:
            return i
    return -1
n = int(input("Enter the number of students: "))
student_id = []
for i in range(n):
    id = int(input("Enter the student id: "))
    student_id.append(id)
id_to_search = int(input("Enter the student id to search: "))
index = linear_search(student_id, id_to_search)
if index == -1:
    print("Student id not found")
else:
    print("Student id found at position: ",index+1)