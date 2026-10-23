
# num = int(input("Enter any number: "))
# sum = 0
# temp = num

# while num > 0:
#     rem = num % 10
#     sum = sum + rem ** 3
#     num = num // 10

# if temp == sum:
#     print("It is an Armstrong number")
# else:
#     print("It is not an Armstrong number")




# #addition of the take inputs


# num = int(input("Enter any number: "))
# total = 0

# while num > 0:
#     rem = num % 10
#     total = total + rem
#     num = num // 10

# print("Addition of digits is:", total)


# # multiplications

# num = int(input("Enter any number: "))
# mul = 1

# while num > 0:
#     rem = num % 10
#     mul = mul * rem
#     num = num // 10

# print("Multiplication of digits is:", mul)

# Armstrong number 
def show(num):
    sum=0
    temp=num
    digit=len(str(num))
    while num > 0:
        rem=num%10
        sum=sum+rem**digit
        num=num//10
    if temp == sum:
        print("Armstrong")
    else:
        print("Not Armstrong")


   
