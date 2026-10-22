#file handling = it  is used to handles the data and store the files permanantly
# difference between append mode and write mode  
# remode 
# there ar 4 mides in the file handling=1.read mode   #  2 append mode     3. write   4.create(x)


f=open("demo1.txt","w")
f.write("hello my name is sanika")
f.close()

file=open("demo1.txt","r")
print("file_name",file.name)
print("readable_mode",file.readable())
print("writable_mofde",file.writable())
print("file_closed",file.closed)
file.close()

f=open("demo1.txt","r")
print(f.read())
f.close()

# write dat in to files using append mode but existing data is automatically removed
f=open("demo1.txt","w")
f.write("hello my name is veda")
f.close()

#write dat tinto files using append method  but existing data vstill remainning
f=open("demo1.txt","a")
f.write("hello my name is veda\n")
f.write("i am from pune")
f.close()


# read lines
f=open("demo.txt","r")           #read only ine line
print(f.readline())

#read the two lines

f=open("demo.txt","r")
print(f.readline())
print(f.readline())

#create new file using x
f=open("demo.txt","x")



#close file
 
f=open("demo.txt","r")
print(f.readline())
f.close()

f=open("demo.txt","r")
print(f.readline())


f=open("demo.txt","w")
print(f.write("i am sanika"))