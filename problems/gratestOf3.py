a,b,c=map(int,input().split())
if(a>=b and a>=c):
    print("The greatest is:",a)
elif(b>=a and b>=c):
    print("The Greatest is:",b)
else:
    print("The Greatest is:",c)