a=[1,23,4,5,6,8,4,6,5,5,7,8,9,3,4,10]
a.append(50)
print("add value",a)
a.extend([55,56,57,58,59,60])
print("extent more value",a)
a.insert(3,900)
print("insert value change",a)
a.sort()
print("acending order",a)
a.reverse()
print(a)
c=a.index(9)
print(c)
f=a.remove(5)==1
print(a)
