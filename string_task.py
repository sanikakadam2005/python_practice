
#1. to check the given string is anagram or not  without using the inbuilt functions
str1=input("enter the string1:")
str2=input("enter the string2:")
if len(str1)!=len(str2):
    print("Not Anagram")
else:
    for ch in str1:
        found=0
    for i in range(len(str2)):
        if ch==str2[i]:
            found=1
            str2=str2[:i]+str2[i+1:]
            break
    if found==0:
        print("Not Anagram")
    else:
        print("Anagram")




# 2.to reverse a given string eg. python 
#method1
# string=input("enter the string:")
# str=string[ : :-1]
# print(str)

#method 2
# string=input("enter the string:")
# rev=" "
# for ch in string:
#     rev=ch+rev
# pytgprint(rev)

#3."hello how are you" reverse this string 
# str="hello how are you"
# str1=str[ : :-1]
# print(str1)


#4.# 4. input=krishna    output=k|r|i|s|s|n|a

# str1 = input("Enter a string: ")
# result = ""
# count = 0

# for ch in str1:
#     if count == 0:
#         result = ch
#     else:
#         result = result + "|" + ch

#     count = count + 1

# print(result)



#5 count the frequency  of the given string 

# str1 = input("Enter a string: ")

# for ch in str1:
#     count = 0
#     duplicate = 0

#     for x in str1:
#         if x == ch:
#             count = count + 1

#     for y in str1:
#         if y == ch:
#             if y == ch:
#                 break

#     for z in str1:
#         if z == ch:
#             break

#     for x in str1:
#         if x == ch:
#             break

#     print(ch, "=", count)


#6.
# s = input("Enter a string: ")

# for i in range(len(s)):
#     print(s[i], "  +ve index =", i, "  -ve index =", i - len(s))


# 7 to check the  no. is palindrome or not  
# string=input("enter the string:")
# string1=string
# rev=" "
# for ch in string:
#     rev=ch+rev
# print(rev)
# if string1==rev:
#     print("palindrome")
# else:
#     print("not palindrome")

#8     # 11-input-hello      output=HELLO    without using upper method
# string=input("enter the string:")
# result=" "
# for ch in string:
#     if 'a'<=ch<= 'z':
#         result =result+chr(ord(ch)-32)
#     else:
#         result=result+ch
# print(result)

#9.  input=HELLO   output+hello

# string = input("Enter the string: ")
# result = ""

# for ch in string:
#     if 'A' <= ch <= 'Z':
#         result = result + chr(ord(ch) + 32)
#     else:
#         result = result + ch

# print(result)