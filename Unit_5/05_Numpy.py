import numpy as np

arr=np.array([1,2,3,4,5])
b=arr
print(b)
# if you make change value in b it will also change in arr. b acts a pointer to arr
b[0]=100
print(arr)

# Use copy function to copy one array into another
a=np.array([5,6,7,8,9])
b1=a.copy()
print(b1)
b1[0]=100
print(b1)
print(a)

