
#1. to check the given string is anagram or not  without using the inbuilt functions
# str1=input("enter the string1:")
# str2=input("enter the string2:")
# if len(str1)!=len(str2):
#     print("Not Anagram")
# else:
#     for ch in str1:
#         found=0
#     for i in range(len(str2)):
#         if ch==str2[i]:
#             found=1
#             str2=str2[:i]+str2[i+1:]
#             break
#     if found==0:
#         print("Not Anagram")
#     else:
#         print("Anagram")




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
# print(rev)

#3."hello how are you" reverse this string 
# string=input("enter a string:")
# word=""
# result=""
# for i in string:
#     if i!=" ":
#         word=word+i
#     else:
#         result=word + " " + result
#         word=" "
# result=word + " " + result
# print(result)    

#4.# 4. input=krishna    output=k|r|i|s|s|n|a

# str=input("enter the string")
# for i in range(len(str)):
#     if i<len(str)-1:
#         print(str[i],end="|")
#     else:
#         print(str[i])



#5 count the frequency  of the given string 
# string=input("enter the string:")
# frequency={ }
# for ch in string:
#     if ch in frequency:
#         frequency [ch]+=1
#     else:
#         frequency[ch]=1
# print(frequency)


#6.# 6.imput=python   output=  chr    +ve index       -ve indexing --  using loop
# s = input("Enter a string: ")

# for i in range(len(s)):
#     print(s[i], "  +ve index =", i, "  -ve index =", i - len(s))


# 7 to check the  no. is palindrome or not  
# string=input("enter the string:")
# string1=string
# rev=""
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