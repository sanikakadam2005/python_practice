#set= it is unordered collection of the unique elements
# indexing and slicing can not be applicable on the set
# remove the duplicate elementsnin the set

s={1,4,6,3,7,2,9,5}
print(s)

#create empty set
set1=set()


#adding element to the set
set2={'abc',2,3,'xyz'}

set2.add(10)
print(set2)

#removing the element of the set
set2.remove(2)
print(set2)

# pop()-it is remove the by default last element of the set

flowers={"rose","lotus","lily"}
flowers.pop()
print(flowers)

#discard()-it remoive the perticular element and print the removed element

flowers.discard("rose")
print(flowers)

#update()-it used to add the elements from  the another set
a={"apple","banana","gava"}

#Union()-union is used to merge both set in main set

a={"rose","lily","lotus"}
b={"python","javaa","c"}
c=a.union(b)
print(c)

# interdection()- it returns the only same elements of the tow sets

s1={10,20,30,40}
s2={30,40,50,60}
c=s1.intersection(s2)
print(s1)

#difference()-only prints the unique items in the first set
c=s1.difference(s2)
print(c)


#symmetric_difference()-it is used to analize thge both sets and disply only unique items from the both sets

x={"a","b","c"}
y={"x","y","z","a","b"}

z=x.symmetric_difference(y)
print(z)


#issubset()- it is used to print the true when the all elements oif the A is present in the set B so we can use this method
a={"lotus","lily","rose"}
b={"lily"}
print(b.issubset(a))

#intersection_update()
x={"a","b","c"}
y={"c","d","e"}
z={"f","g","c"}

x.intersection_update(y,z)
print(x)


