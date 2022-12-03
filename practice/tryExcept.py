try:
    x=int(input("Input an Intiger :"))
    print(x)
except ValueError:
    print("value not an interger")
else:
    print("nothing went worng")
finally:
    print("try except finished")