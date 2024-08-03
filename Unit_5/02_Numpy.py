import numpy as np
arr=np.array([
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
    ])
print(arr)
print(np.sin(arr))
print("Max")
print(arr.max())
print(arr.max(axis=1))
print(arr.max(axis=0))
print("Slicing")
print(arr[1:3,0:2])

arr2=np.linspace(10,20,20).reshape(4,5)
print("Reshaped")
print(arr.reshape(4,3))
print(arr2)


'''
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
'''
#order must be one of 'C', 'F', 'A', or 'K' (got 'T')
#C=row Major
for x in np.nditer(arr,order='K'):
    print(x)
# for x in np.nditer(arr,order='C'):
#     print(x)
# for x in np.nditer(arr,order='A'):
#     print(x)
# for x in np.nditer(arr,order='K'):
#     print(x)
# print(np.nditer(arr))
# print(np.nditer(arr,order='F'))