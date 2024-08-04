import numpy as np

# Mathematics
a=np.array([1,2,3,4,5,6])
print(a)
print(a+2)
print(a*2)
print(a/2)
print(a-2)
print(a**2)
print(a//2)
b=np.array([7,8,9,10,11,12])
print(np.sin(a))
print(np.cos(a))
print(np.tan(a))
print(a+b)
print(a*b)

# Linear Algebra
aa=np.ones((2,3))
bb=np.full((3,2),2)
print(aa)
print(bb)
print(aa.dot(bb))
print(np.matmul(aa,bb))

# Find determinant
cc=np.random.randint(1,100,(5,5))
c=np.identity(3)
print(np.linalg.det(c))
print(np.linalg.det(cc))


# Statistics
st=np.array([[1,2,9],[4,5,6]])

# Min
print(np.min(st))
print(np.min(st,axis=0))
print(np.min(st,axis=1))

# Max
print(np.max(st))
print(np.max(st,axis=0))
print(np.max(st,axis=1))

# Sum
print(np.sum(st))

# sqrt
print(np.sqrt(st))

# Reorganizing arrays
# reshape function
be=np.arange(9)
print(be.reshape(3,3))

# Vertically Stacking vectors

v1=np.arange(10)
v2=np.arange(10,20)
print(np.vstack([v1]))
print(np.vstack([v1,v2]))
print(np.vstack([v1,v2,v1,v2,v1,v2]))

# Horizontally stacking array
print(np.hstack([v1]))
print(np.hstack([v1,v2]))
print(np.hstack([v1,v2,v1,v1]))
