year = int(input())
if(year%4==0):
    if(year%100==0):
        if year%400:
            print("Leap Year")
        else:
            print("Not a Leap Year")
    else:
        print("Leap year")
else:
    print("Not a leap Year")