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
    print("it is noit armstrong number")