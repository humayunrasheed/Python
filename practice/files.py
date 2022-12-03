file=open("C:/Users/Humayun/Desktop/Python/practice/example.txt","r")
# r means only read
# w means write and edit
# a means append
# r+ for read and write
print(file.readable())
print(file.readline())
for lines in file.readlines():
    print(lines)
file.close()
# writing in file
file=open("C:/Users/Humayun/Desktop/Python/practice/example2.txt","w")
file.write("hello we have created a new file and witten")
file.close()
# appending file
file=open("C:/Users/Humayun/Desktop/Python/practice/example2.txt","a")
file.write("\nNew text is written")
file.close()