
class Node:
    def __init__(self,data,prev=None,next=None):
        self.data = data
        self.prev = prev
        self.next = next
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def display(self):
        temp = self.head
        while(temp):
            print(temp.data,end="-->")
            temp = temp.next
        print("None")
    def reverseDisplay(self):
        temp = self.tail
        while(temp):
            print(temp.data,end="-->")
            temp = temp.prev
        print("None")
    def insertBegin(self,element):
        newNode = Node(element)
        if self.head == None:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
    def insert(self,element):
        newNode = Node(element)
        if self.head == None:
            self.head = newNode
            self.tail = newNode
        else:
            temp = self.head
            while(temp.next):
                temp = temp.next
            temp.next = newNode
            newNode.prev = temp
            self.tail = newNode
    def insertEnd(self,element):
        newNode = Node(element)
        if self.head == None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode
    def insertP(self,element,position):
        newNode = Node(element)
        if self.head == None:
            self.head = newNode
            self.tail = newNode
        else:
            temp = self.head
            for i in range(position-1):
                temp = temp.next
            newNode.next = temp.next
            newNode.prev = temp
            temp.next.prev = newNode
            temp.next = newNode
    def deleteBegin(self):
        if self.head == None:
            print("List is empty")
        else:
            temp = self.head
            self.head = self.head.next
            self.head.prev = None
            del temp
    def deleteEnd(self):
        if self.head == None:
            print("List is empty")
        else:
            temp = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
            del temp
    def deleteP(self,position):
        if self.head == None:
            print("List is empty")
        else:
            temp = self.head
            for i in range(position-1):
                temp = temp.next
            temp.next = temp.next.next
            temp.next.prev = temp
    def LargestElement(self):
        if(self.head == None):
            print("List is empty")
            return
        largest = 0
        temp = self.head
        while(temp):
            if(temp.data > largest):
                largest = temp.data
            temp = temp.next
        print("Largest element is: ",largest)
a= True
dl = DoublyLinkedList()
while(a):
    print("1. Insert at the beginning")
    print("2. Insert at the end")
    print("3. Insert at a given position")
    print("4. Delete at the beginning")
    print("5. Delete at the end")
    print("6. Delete at a given position")
    print("7. Display the list")
    print("8. Reverse display the list")
    print("9. Delete the List")
    print("10. Largest element in the list")
    print("0. Exit")
    choice = int(input("Enter your choice: "))
    if(choice == 1):
        print("Insert at the beginning")
        n = int(input("Enter the element:"))
        dl.insertBegin(n)
    elif(choice == 2):
        print("Insert at the end")
        dl.insertEnd(int(input("Enter the element:")))
    elif(choice == 3):
        print("Insert at a given position")
        dl.insertP(int(input("Enter the element:")),int(input("Enter the position:")))
    elif(choice == 4):
        print("Delete at the beginning")
        dl.deleteBegin()
    elif(choice == 5):
        print("Delete at the end")
        dl.deleteEnd()
    elif(choice == 6):
        print("Delete at a given position")
        dl.deleteP(int(input("Enter the position:")))
    elif(choice == 7):
        print("Display the list")
        dl.display()
    elif(choice == 8):
        print("Reverse display the list")
        dl.reverseDisplay()
    elif(choice == 9):
        dl.head = None
        dl.tail = None
        print("List deleted")
    elif(choice == 0):
        a = False
        
    elif(choice == 10):
        dl.LargestElement()
    else:
        print("Invalid choice")