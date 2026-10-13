list=[10,20,30,40,50]
print(list)


#insert()-  used to add the elements on the perticular indexing
list1=[10,20,30,40]
list1.insert(2,60)
print(list1)

#index()- it is used to find the stored elements indexing

print(list1.index(10))

#append()- it is used to add the element at end of the list
list=[10,20,30,40]
list.append(80)
print(list)


# pop() - deletes the last element of the list

numbers = [10, 20, 30, 40]
numbers.pop()
print(numbers)


#remove()-it is used to remove the pertilar number in the list

number=[10,20,30,40]
number.pop(2)
print(number)

#extend()-by using the extend method we can merge 2 list

num=[10,20,30,40]
num1=[50,60,70]
num.extend(num1)
print(num)

#reverse()- to print the list in trhe reverse order

n=[10,20,30,40]
n.reverse()
print(n)

#sum()-it is used to print sum of the all elements of the list

n=[10,20,30,40]
print(sum(n))

#sorted-it is used to sort the order by accending or decending order
n=[40,50,10,20,30]
n.sort()
print(n)

# count()-it is usedc to how many times numbers are present in the list
n=[1,2,3,445,6]
print(n.count(2))

# slice()-
n=[10,20,30,40]
print(n[ : :2])

# min- in is used to print the miniumum value in the list
n=[10,20,30,40]
print(min(n))

#max-to print the max value
n=[10,20,30,40]
print(max(n))

#len()
n=[10,20,30,40]
print(len(n))

