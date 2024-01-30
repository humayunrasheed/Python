from collections import deque
d = deque()
choice = 0
while(choice != 7):
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Peek")
    print("4. Display")
    print("5. Remove the element")
    print("6. Enter N elements")
    print("7. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        d.append(int(input("Enter element: ")))
    elif choice == 2:
        print("Dequeued element is",d.popleft())
    elif choice == 3:
        print(d[0])
    elif choice == 4:
        print(d)
    elif choice == 5:
        d.remove(int(input("Enter element to remove: ")))
    elif choice == 6:
        n = int(input("Enter the number of elements: "))
        for i in range(n):
            d.append(int(input("Enter element: ")))
    elif choice == 6:
        break
    else:
        print("Invalid choice")