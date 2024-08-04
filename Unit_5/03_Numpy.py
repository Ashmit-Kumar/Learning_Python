'''
Why use numpy over List
1) List are very slow meanwhile numpy are very fast
In numpy you can specify int32 or int16 or int8 according to your needs as it takes less space as compared to list it is faster

In list a single integer requires lot more space than a numpy 

2) In numpy compiler can read faster as there are less bytes of memeory

3)In numpy compiler does not have to perform typecheck when iterating through object/elements evertime as in numpy only stores one type of data in a single array

4)Numpy utilises contiguous memory  while list is scattered around

Q) How are list differnt from numpy
Ans) List: In list we can do insertion, deletion , appending, concatenation etc.

Numpy: In numpy we can do insertion, deletion , appending, concatenation etc. and lots of more stuff.


Application of numpy
1)Mathmetics(MATLAB Replacement)
2)Plotting(MatPlotLib)
3) Backend(Pandas, Digital Photography, Connect 4,)
4)Machine Learning

Data types in numpy
i - integer
b - boolean
u - unsigned integer
f - float
c - complex float
m - timedelta
M - datetime
O - object
S - string
U - unicode string
V - fixed chunk of memory for other type ( void )
'''

import numpy as np

a=np.array([1,2,3,4,5]) # To create a numpy array when we already know the elements

b=np.array(['a','b','c','d'])
c=np.array([9,8,7,6,5])
d=np.array([1,2,3])
e=np.array([1,2,3])

'''When you want to store data type of the elemet in which you want to store the value we use 
   np.array([1,2,3,4], dtype='int16')
'''
dt=np.array([11,12,14,13],dtype='int8')
print('dtype of array')
print(dt)
print(dt.dtype)
print(dt[0,1,-1])

#To multiply two array 
print(a*c) # this will multiply element present at index i in array a to element present in index i in array c 
# both array should be of same size
d1=a.dot(c) #this will add that new array
print(d1)
print(d.dot(e))
f=np.array(['A',2,3])
f1=np.array(['B',2,3])

# type function
print(type(e))
print(e.dtype) # this function gives the data type of the element inside e array

# ndim fun: this function returns the dimension of the array
# Syntax= a=[[1,2],[1,2]]
#         a.ndim
g=np.array([[1,2,3],[1,2,3]])
print(g.ndim)

g1=np.array([1,2,3])
g2=np.array([[[1,2,3],
              [1,3,4],
              [4,5,6]],
             [[1,2,3],
              [1,3,4],
              [4,5,6]]])
# Shape function:
# Syntax= a.shape  for 1 d array it returns (5,) 
print(g.shape)
print(g1.shape)
print(g2.shape)
print(g2)

# Size function
h=np.array(['A','B','C','D'])
h1=np.array([1.0,2,0,3,0],dtype='float64')
print(h1.itemsize)
print(g.size)
print(g.itemsize)
print(g2.size)
print(g2.itemsize)
dt = np.dtype([('name', np.str_, 16), ('grades', np.float64, (2,))])
print(dt)


