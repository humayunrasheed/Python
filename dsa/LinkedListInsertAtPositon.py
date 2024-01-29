class Node :
    def __init__(self,data,next=None):
        self.data = data
        self.next = next
class LinkedList:
    def __init__(self):
        self.head = None
    def display(self):
        temp = self.head
        while(temp):
            print(temp.data,end="-->")
            temp = temp.next
        print("None")
    def insertAtPosition(self,element,position):
        newNode = Node(element)
        if self.head == None:
            self.head = newNode
        elif position -1 == 0:
            newNode.next = self.head
            self.head = newNode
        else:
            temp = self.head
            pos = 0
            while(temp.next and pos < position-1):
                temp = temp.next
                pos += 1
            newNode.next = temp.next
            temp.next = newNode
n = int(input("Enter the number of elements: "))
l1 = LinkedList()
for i in range(n):
    l1.insertAtPosition(int(input("Enter element: ")),int(input("Enter position: ")))
l1.display()