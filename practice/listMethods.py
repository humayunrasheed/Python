list1=[1,3,2,8,9,4,5,6]
list1.sort()
print(list1)
many="something"
list2=["hello","may",many]
list1.extend(list2)
print(list1)
print(list2)
list2.append('cherry')
print(list2)
list2.insert(1,"how many")
print(list2)
list2.remove(many)
print(list2)
list1.clear
print(list1)
print(list2.index('cherry'))
print(list2.count("cherry"))
print(list2.count("l"))
list2.sort()
list2.reverse()
print(list2)
list3=list2.copy()
list3.pop()
print("list 3 is ",list3)
list3.pop(2)
print("list 3 is ",list3)
del list3[0]
#del list3 #not avaliable in the code
print(list3)