#
# import numpy as np
# arr=np.array([1,2,3,4,5])             #it is used for scientific calculations
# print(arr)

# import numpy
# arr=numpy.array([1,2,3,4,5])
# print(arr)


# tupres of array
# 0-D= array(42)==scaler
# 1D=   []   =vector
# 2D=[[],[]]  =matrix
# multidimentional=[[[],[],[]]]= tensor


# import numpy as np
# arr1=np.array(42)
# arr2=np.array([1,2,3,4,5])
# arr3=np.array([[1,2,3],[4,5,6]])
# arr4=np.array([[[1,2],[3,4],[5,6]]])
# print(arr1)
# print(arr2)
# print(arr3)
# print(arr4)

# import numpy as np
# arr1=np.array([1,2,3,4])
# arr2=np.array([1.2,2.45,3.45,4.56])
# print(arr1.dtype)
# print(arr2.dtype)


import numpy as np

x = np.array([3, 5])
y = np.array([2, 5])

print("Original numbers")
print(x)
print(y)

print("Comparison - Greater")
print(np.greater(x, y))

print("Comparison - Greater Equal")
print(np.greater_equal(x, y))

print("Comparison - Less")
print(np.less(x, y))

print("Comparison - Less Equal")
print(np.less_equal(x, y))




# import numpy as np
# a=np.array([11,22,33,44,55,66,77,88,99,10,11,12])
# na=a.reshape(4,3)
# print(na)

# naa=a.reshape(2,2,3)
# print(naa)

# for x in a:     # dir 1D
#     print(x)

# import numpy as np
# a=np.array([[[1,2,3],[1,2,3],[1,2,3]]])
# for i in a:
#     print(i)
# for i in np.nditer(a):
#     print(i)
# a=np.array([1,2,3,4,5,4,4])
# n=np.where(a==4)
# print(n)


# import numpy as np
# a=np.array([1,2,3,4,5,6,7,8])
# x=np.where(a%2==0)
# print(x)
# print(np.sort(a))