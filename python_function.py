<<<<<<< HEAD
# def display():
#     print("hello world")

# display()


# def display():
#     print("good morning")

# display()


# def display():
#     print("good afternoon")

# display()



# # by passing the parameters
# def add(a,b):
#     print(a+b)
# add(4,5)

# # reverse number
# num=int(input("enter the number:"))
# def reverse(num):
#     rev=0

#     while num > 0:
#         rem=num%10
#         rev=rev*10+rem
#         num=num//10
#     return rev
# print("reverse number is",reverse(num))

# # Armstrong number
# num=int(input("enter the number"))
# sum=0
# temp=num

# while num>0:
#     rem=num%10
#     sum=sum+rem**3
#     num=num//10

# if temp == sum:
#     print("it is armstrong number")
# else:
#     print("it is not armstrng no")

# # write difference between print and return

# #lambda function /Anonymous


# #gretest of two 

# greater=lambda x,y:x if x>y else y
# print("gretest number is",greater(5,10))


# #postive or negative

# num=lambda x: "positive " if  x>0 else "negative"
# print(num(5))

# #square
# num=lambda x:x*x
# print("square is",num(5))


# #cude
# num=lambda x:x*x*x
# print("cude is",num(5))


# #even odd
# even=lambda x:"even" if x%2==0 else "odd"
# print(even(5))

# #voting
# a=lambda x :"eligible" if x>18 else "not eligible"
# print(a(45))

# #pass and fail
# p=lambda x : "pass" if x>35 else "fail"
# print(p(56))

# map function
#to print the square
# def sq(x):
#     return x*x
# t=(1,2,3,4,5,6,7)
# u=map(sq,t)
# print(list(u))

# # to printthe add in the ach element 0f 10
# def add(x):

# use of pass keyworld = pass keyword is used to the  to reserve the location
# def demo():
#     pass
# demo()

#function argumenta= there 4 types of arguments that we can provide in a function

#1.default argument
# def name(fname,mname="vijay",lname="kadam"):
#     print("hello,", fname,mname,lname)
# name("sanika")


# 2.keyword argument

# def name(fname,mname,lname):
#     print("hello",fname,mname,lname)
# name(mname="vijay",fname="sanika",lname="kadam")

#3.variable length argument
#  a. arbitary arguments
def avg(*numbers):
    sum=0
    for i in numbers:
        sum=sum+i
    print("Avg is",sum/len(numbers))
avg(1,4,5,6)

#   b. keyword arbitary bargument
def name(**name):
    print(type(name))
    print("hello",name["fname"],name["mname"],name["lname"])
name(mname="vijay",lname="kadam",fname="sanika")


#4.required argument


=======
# def display():
#     print("hello world")

# display()


# def display():
#     print("good morning")

# display()


# def display():
#     print("good afternoon")

# display()



# # by passing the parameters
# def add(a,b):
#     print(a+b)
# add(4,5)

# # reverse number
# num=int(input("enter the number:"))
# def reverse(num):
#     rev=0

#     while num > 0:
#         rem=num%10
#         rev=rev*10+rem
#         num=num//10
#     return rev
# print("reverse number is",reverse(num))

# # Armstrong number
# num=int(input("enter the number"))
# sum=0
# temp=num

# while num>0:
#     rem=num%10
#     sum=sum+rem**3
#     num=num//10

# if temp == sum:
#     print("it is armstrong number")
# else:
#     print("it is not armstrng no")

# # write difference between print and return

# #lambda function /Anonymous


# #gretest of two 

# greater=lambda x,y:x if x>y else y
# print("gretest number is",greater(5,10))


# #postive or negative

# num=lambda x: "positive " if  x>0 else "negative"
# print(num(5))

# #square
# num=lambda x:x*x
# print("square is",num(5))


# #cude
# num=lambda x:x*x*x
# print("cude is",num(5))


# #even odd
# even=lambda x:"even" if x%2==0 else "odd"
# print(even(5))

# #voting
# a=lambda x :"eligible" if x>18 else "not eligible"
# print(a(45))

# #pass and fail
# p=lambda x : "pass" if x>35 else "fail"
# print(p(56))

# map function
#to print the square
# def sq(x):
#     return x*x
# t=(1,2,3,4,5,6,7)
# u=map(sq,t)
# print(list(u))

# # to printthe add in the ach element 0f 10
# def add(x):

# use of pass keyworld = pass keyword is used to the  to reserve the location
# def demo():
#     pass
# demo()

#function argumenta= there 4 types of arguments that we can provide in a function

#1.default argument
# def name(fname,mname="vijay",lname="kadam"):
#     print("hello,", fname,mname,lname)
# name("sanika")


# 2.keyword argument

# def name(fname,mname,lname):
#     print("hello",fname,mname,lname)
# name(mname="vijay",fname="sanika",lname="kadam")

#3.variable length argument
#  a. arbitary arguments
# def avg(*numbers):
#     sum=0
#     for i in numbers:
#         sum=sum+i
#     print("Avg is",sum/len(numbers))
# avg(1,4,5,6)

# #   b. keyword arbitary bargument
# def name(**name):
#     print(type(name))
#     print("hello",name["fname"],name["mname"],name["lname"])
# name(mname="vijay",lname="kadam",fname="sanika")


#4.required argument

def greet(name, message="Hello"):
    print(message, name)

greet("Sanika")
>>>>>>> cf71758 (add the requirement argument example)
