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
    def insertBegin(self,element):
        newNode = Node(element)
        if self.head == None:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode
    def insertEnd(self,element):
        newNode = Node(element)
        if self.head == None:
            self.head = newNode
        else:
            temp = self.head
            while(temp.next):
                temp = temp.next
            temp.next = newNode
    
    def occur(self,element):
        temp = self.head
        count = 0 
        while(temp):
            if temp.data == element:
                count += 1
            temp = temp.next
        print(count)
    def sort(self):
        temp = self.head
        while(temp):
            temp2 = temp.next
            while(temp2):
                if temp.data > temp2.data:
                    temp.data,temp2.data = temp2.data,temp.data
                temp2 = temp2.next
            temp = temp.next
            
l1 = LinkedList()
l1.head = Node(1)
second = Node(2)
third = Node(3)
l1.head.next = second
second.next=third
third.next=None
l1.insertBegin(0)
l1.display()
l1.occur(1)
l1.insertEnd(4)
l1.display()