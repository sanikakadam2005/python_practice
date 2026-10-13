"""i=1
while(i<10):
    print(i)
    i+=1
"""

num=int(input("enter num:"))
rev=0
while(num>0):
    rem=num%10
    rev=rev*10+rem
    num=num//10
print("reverse number is:",rev)