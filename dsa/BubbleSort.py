def BubbleSort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if(arr[j]>arr[j+1]):
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr
p = int(input("Enter the number of elements: "))
arr = []
for i in range(p):
    x = int(input("Enter the element: "))
    arr.append(x)
print("The array is: ",arr) 
print("The sorted array is: ",BubbleSort(arr))