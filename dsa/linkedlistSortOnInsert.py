class Node:
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
            temp=temp.next
        print()
    def insertAndSort(self,element):
        newNode = Node(element)
        if self.head == None:
            self.head = newNode
        elif self.head.data > element:
            newNode.next = self.head
            self.head = newNode
        else:
            temp = self.head
            while(temp.next and temp.next.data < element):
                temp = temp.next
            newNode.next = temp.next
            temp.next = newNode
n= int(input("Enter the number of elements: "))
l1 = LinkedList()
for i in range(n):
    l1.insertAndSort(int(input("Enter element: ")))
l1.display()