class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    def display(self):
        temp = self.front
        while(temp):
            print(temp.data,end="-->")
            temp = temp.next
        print("None")
    def enqueue(self,element):
        newNode = Node(element)
        if self.front == None:
            self.front = newNode
            self.rear = newNode
        else:
            self.rear.next = newNode
            self.rear = newNode
    def dequeue(self):
        if self.front == None:
            print("Queue is empty")
        else:
            NodetoPop = self.front
            self.front = self.front.next
            print("Dequeued element is",NodetoPop.data)
            NodetoPop.next = None
    def peek(self):
        if self.front == None:
            print("Queue is empty")
        else:
            print(self.front.data)
q = Queue()
while(True):
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Peek")
    print("4. Display")
    print("5. Enter N elements")
    print("6. Exit")
    try:
        ch = int(input("Enter your choice: "))
        if ch == 1:
            q.enqueue(int(input("Enter element: ")))
        elif ch == 2:
            q.dequeue()
        elif ch == 3:
            q.peek()
        elif ch == 4:
            q.display()
        elif ch == 5:
            n = int(input("Enter the number of elements: "))
            for i in range(n):
                q.enqueue(int(input("Enter element: ")))
        elif ch == 6:
            break
        else:
            print("Invalid choice")
    except:
        print("Invalid choice")