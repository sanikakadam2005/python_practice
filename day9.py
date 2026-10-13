l=[10,20.5,"hello",True,3+5j]
print(l)
print(type(l))
print(id(1))

print(l[3])
print(l[-3])

# Nested list

l1=[10,20.5,"hello",[10,20,30],["Virat","Rohit"],True,3+5j]
print(l1[4][0][2])

# slicing   it used for the reverse the list without using the in-build functions

a=[10,20,30,40,50,60]
print(a[ : :2])
print(a[2:5:2])