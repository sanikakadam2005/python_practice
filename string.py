# str1='python'
# print(str1)

# str2=" hello python"
# print(str2)

# str3=''' good morning
#  students'''
# print(str3)

#indexing and slicing

# str="hello world"
# print("positive")
# print(str[1])
# print(str[4])
# print(str[7])
# print(str[10])

# print("negative")
# print(str[-3])
# print(str[-4])
# print(str[-11])


# slicing

# str="hello world"
# print(str[1:4])
# print(str[4:8])
# print(str[7:11])
# print(str[3:7])

# print(str[0:7:3])
# print(str[6:10:3])
# print(str[6:9:2])
# print(str[7:9:1])



# string functions

# capitalize
# str="welcome"
# str1=str.capitalize()
# print(str1)
# print(id(str1))  # memory location
# print(id(str))

# #isupper   it rreturn the value is true or false

# str="WELCOME"
# str1=str.isupper()
# str2=str.lower()    # it converts the in to lower case
# print(str1)
# print(str2)

# # islower   it return the value is true or false
# str="hello"
# str1=str.islower()
# str2=str.upper()
# print(str1)
# print(str2)

#len()
# str="welcome"
# print(len(str))

#replace()
# str = "Java is a programming language"
# str3=str.replace("Java","python")
# print(str3)

#join()
# str=""
# list=["h","e","l","l","o"]
# str2=str.join(list)
# print(str2)

#index= is used to access the priority from forward to backword
#it returns the first occured sring
#find= if the variable is cant present in the string then print the -1 by default an index ,ethod give the error

# str="communication"
# str2=str.index("c")    #Communication
# print(str2)
# str3=str.rfind("c")                      # diff bet find and rfind   and  find and index
# print(str3)

# str="Welcome to the python"
# str2=str.index("p",13,21)
# print(str2)



#partition ()   retun in the value in tuple  it can be seoarate the according to the condition

# str="python is a programming language"
# str2=str.partition("is")
# print(str2)

#split()   it is used to split the each and evry word present in the give n sttements
# str="python is a programming language"
# str2=str.split()
# print(str2)


#count()-- it used to the find the vowels in the given string
# str="python is a programming language"
# str2=str.count("pro",6,15)
# print(str2)


#count

# s="programming"
# count=0
# for ch in s:
#     if(ch=='a' or ch=='e' or ch=='i'or ch=='o'or ch=='u'):
#         count +=1
    
# print(count)

# s="communication"
# count=0
# for ch in s:
#     if(ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u'):
#         count +=1
# print(count)

# s="programming"
# for ch in s:
#     if(ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u'):
#         print("total count of the vowels is:,ch")


#3. s="python_is_programming_land"  to count th spaces


# s="python is programming lang"
# count=0
# for ch in s:
#     if ch==" ":
#         count +=1
# print("total white sopace in s",count)


# s="programming language"
# count=0
# for ch in s:
#     if(ch=="a"):
#         count +=1
# print(count)

#task=1.  to check the given styring is anagram or not      without using the inbuilt funcytions

# 2.to reverse a given string eg. python
# 3."hello how are you" reverse this string      you are how hello
# 4. input=krishna    output=k|r|i|s|s|n|a

# 5 count the frequency  of the give n string     frequency  = how many times elements ar comes in this string
# 6.imput=python   output=  chr    +ve index       -ve indexing --  using loop

# 7 to chech the palindrome or not   
   
s="mom"
s1=s[ : :-1]
if(s==s1):
    print("string is pallindrome")
else:
    print("not palindrome")

    # 11-input-hello      output=HELLO    without using upper method
    #12 input-HELLO      output-hello     witjout using in build method
    


