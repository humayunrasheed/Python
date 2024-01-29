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
dl = DoublyLinkedList()
n = int(input("Enter the number of elements: "))
for i in range(n):
    dl.insertBegin(int(input("Enter element: ")))
dl.display()
dl.reverseDisplay()