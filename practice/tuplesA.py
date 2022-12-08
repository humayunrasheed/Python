mytuple= ("max",34)
a= tuple(("boxton",78,"hello"))
item= mytuple.index(34)
print(item)
if "max" in mytuple:
    print("yes")
else:
    print("no")
print(len(mytuple))
print(a.count(78))
num=(1,2,3,4,5,6,7,8,9)
b=num[0:6:2]
print(b,type(b))
c=num
print(c)
name,age=mytuple
i1,*i2,i3=num
print(name,age,i1,i2,i3)
#less memory and time using tuple