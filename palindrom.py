# num = int(input("Enter the number: "))
# rev = 0
# temp = num

# while num > 0:
#     rem = num % 10
#     rev = rev * 10 + rem
#     num = num // 10

# print("Reverse number is:", rev)

# if temp == rev:
#     print("Given number is a palindrome")
# else:
#     print("Given number is not a palindrome")



def show(num):
    rev=0
    temp=num

    while num>0:
        rem = num % 10
        rev = rev *10 +rem
        num= num // 10
    print("reverse number is:", rev)
    if temp == rev:
        print("palindrome")
    else:
        print("not palindrome")