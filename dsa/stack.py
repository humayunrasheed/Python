class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next
class Stack:
    def __init__(self):
        self.top = None
    def display(self):
        temp = self.top
        while(temp):
            print(temp.data,end="-->")
            temp = temp.next
        print("None")
    def push(self,element):
        newNode = Node(element)
        if self.top == None:
            self.top = newNode
        else:
            newNode.next = self.top
            self.top = newNode
    def pop(self):
        if self.top == None:
            print("Stack is empty")
        else:
            NodetoPop = self.top
            self.top = self.top.next
            print("Popped element is",NodetoPop.data)
            NodetoPop.next = None
            
    def peek(self):
        if self.top == None:
            print("Stack is empty")
        else:
            print(self.top.data)
    def minimum(self):
        if self.top == None:
            print("Stack is empty")
        else:
            temp = self.top
            min = temp.data
            while(temp):
                if temp.data < min:
                    min = temp.data
                temp = temp.next
            print("Minimum element is",min)
a  = Stack()

while(True):
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. Minimum")
    print("6. Exit")
    try:
        ch = int(input("Enter your choice: "))
        if ch == 1:
            a.push(int(input("Enter element: ")))
        elif ch == 2:
            a.pop()
        elif ch == 3:
            a.peek()
        elif ch == 4:
            a.display()
        elif ch == 5:
            a.minimum()
        elif ch == 6:
            break
        else:
            print("Invalid choice")
    except ValueError as error:
        print("Invalid choice",error)