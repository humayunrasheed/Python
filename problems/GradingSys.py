marks = int(input())
if marks in range(0,101):
    if marks in range(91,101):
        print("S")
    elif marks in range(81,91):
        print("A")
    elif marks in range(71,81):
        print("B")
    elif marks in range(61,71):
        print("C")
    elif marks in range(51,61):
        print('D')
    elif marks in range(41,51):
        print("E")
    else:
        print("E")
else:
    print("Invalid marks")