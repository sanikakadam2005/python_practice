# it is used to add extra functionalities in the function
# it defines by @



# def decor(func):
#     def inner(name):
#         if name=="sunny":
#             print("hello sunny bad morning")
#         else:
#             func(name)
#     return inner
# @decor
# def wish(name):
#     print("hello",name,"good morning")
# wish("ravi")
# wish("himanshu")
# wish("sunny")


# exceptions =10
# decorators=5


# without using decor
def decor(func):
    def inner(name):
        if name=="sunny":
            print("hello sunny bad morning")
        else:
            func(name)
    return inner

def wish(name):
    print("hello",name,"good morning")

decofunction=decor(wish)

wish("durga")
wish("sunny")

decofunction("durga")
decofunction("durga")


#generators

# what
# when use
# where we use
# real life example
# technical example
# practical example

def simple():
    for i in range(1,11):
        yield i
for i in simple():
    print(i) 
 