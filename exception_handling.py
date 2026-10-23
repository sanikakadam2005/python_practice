#An unwanted and unexpected event that disturbs normal flow of program is called exception.abs

#without try-except
# print("stmt-1")
# print(10/0)
# print(10/2)

# #with try-except
# print("stmt 1")
# try:
#     print(10/0)
# except ZeroDivisionError:
#     print(10/2)
# print("stmt 3")


# try:
#     a=int(input("enter number:"))
#     b=int(input("enter number"))
#     c=a/b
# except ZeroDivisionError:
#     print("cant devide with zero")
# except SyntaxErroreError:
#     print(" provide the proper value ")
# except  ValueError:
#     print("cant divide")

try:
    x=int(input("enter no:"))
    y=int(input("enter no:"))
    print(x/y)
except ArithmeticError:
    print("Arithmatic error")
except ZeroDivisionError:
    print("Zerodivision error")   

# difference keywordlengthargument and variablelength argument
# pass keyword