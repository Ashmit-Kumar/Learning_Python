# Acessing/Changing specific elements, rows,columns etc
import numpy as np

a=np.array([
    [1,2,3,4,5,6],
    [7,8,9,10,11,12],
    [13,14,15,16,17,18]],dtype='int8')

# Get a specific element a[r.c]
print(a[1,2])
# it supports negative indexing as well
print(a[-1,-2])
print(a[-2,-2])
print(a[-3,-2])

# Get a specific row
print(a[1,:])

# Get a specific column
print(a[:,2])

# Using fancy indexing 
#  fancy[startindex:endindex:stepsize]
print(a[0,1:5:2])

b=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(b)
print(b[0,1,1])
print(b[1,1,1])

# replace
b[0,1,1]=0
print(b)
b[:,1,:]=[[89,80],[87,76]]
print(b)

# Initializing different types of Arrays


# All zeros matrix
print(np.zeros(5))
print(np.zeros((5,5)))
print(np.zeros((5,5,5)))

# All ones matrix
print(np.ones((5)))
print('ones ')
print(np.ones((5,5)))
print('two d one')
print(np.ones((5,5,5)))

# Any other number
# Symtax np.full((r,c),value)
print(np.full((2,2),4))
print(np.full((3,3,3),2))

# all random matrix
# this does not take a tuple we directly pass value in np.random.rand(r,c) function
print(np.random.rand(4,2))
# random integer values
# syntax= np.random.randint(start_Value,end_value, size=(r,c))
print(np.random.randint(10,100, size=(9,9)))
print("second type")
# syntax= np.random.randint(start_Value,end_value, (r,c))
print(np.random.randint(10,100,(5,5)))
# np.random.randint(10,(3,3))  here 10 will be treated as end value and start value will be zero

# identity matrix
#Syntax np.identity(Size_of_n*n_Matrix)
print(np.identity(3))

# Repeat array
arr=np.array([1,2,3,4,5])
print(np.repeat(arr,3))
# Output [1 1 1 2 2 2 3 3 3 4 4 4 5 5 5]
print(np.repeat(arr,3,axis=0))
arr2=np.array([[1,2,3],[4,5,6]])
print(np.repeat(arr2,3))
print(np.repeat(arr2,3,axis=0))
print(np.repeat(arr2,3,axis=1))

test=np.ones((5,5))
z=np.zeros((3,3))
n=np.full((1,1),9)
print(n)
print(z)
z[1:2,1:2]=n
print(z)
test[1:4,1:4]=z
print(test)



