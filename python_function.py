def display():
    print("hello world")

display()


# by passing the parameters
def add(a,b):
    print(a+b)
add(4,5)

# reverse number
num=int(input("enter the number:"))
def reverse(num):
    rev=0

    while num > 0:
        rem=num%10
        rev=rev*10+rem
        num=num//10
    return rev
print("reverse number is",reverse(num))

# Armstrong number
num=int(input("enter the number"))
sum=0
temp=num

while num>0:
    rem=num%10
    sum=sum+rem**3
    num=num//10

if temp == sum:
    print("it is armstrong number")
else:
    print("it is not armstrng no")

