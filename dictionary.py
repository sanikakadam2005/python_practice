# #empty dictionary
# D1={}
# print(D1)

# #dictinary-- it contains the values in the formas of the keys and values paires
# dic={1:"sanika",2:"asmita"}
# print(dic)

# # Accesing value using keys
# print("first name is "+dic[1])
# print(dic.keys())
# print(dic.values())

# # get()= it is used for the get the values of the item.
# a={1:"ABC",2:"PQR",3:"XYZ",4:"MNO"}
# v=a.get(1)
# print(v)

# #copy()=get the value of the dictionary as it is in the second dictionary

# mydic={
#     "id":101,
#     "name":"sanika",
#     "Age":21
# }
# c=mydic.copy()
# print(c)


# #pop()-it is used for the remoive the data from the dictionary

# mydic.pop("Age")
# print(mydic)

# # sorted - it is used to sort the dictonary by accending or decending order
 a={1:"ABC",2:"PQR",3:"XYZ",4:"MNO"}

# # print sorted list of keys
# print(sorted(a.keys()))
# print(sorted(a.values()))

# # iteams()-it is used to acsess the keys and values at a time
# b=a.items()
# print(b)

# popitem()-remove the last item from the dictonary
a.popitem()
print(a)

# update()-it can be used to add the data in the dictiobary

student = {"name": "Sanika", "age": 21}

student.update({"city": "Sangli", "marks": 85})

print(student)


#setdefault()- it used to set by default values to the dictionary

student1 = {
    "name": "Sanika",
    "age": 21
}

student1.setdefault("city", "sangli")

print(student1)






