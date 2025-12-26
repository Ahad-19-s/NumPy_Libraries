import numpy as np

# 0 dimansional 
a= np.array(23)
print(a)

# 1d 
b= np.array([32,35,56,6])

print(b)

#2d 
c=np.array([[22,1,4],[23,4,2]])
print(c)

# 3 D
d=np.array([[[11,2,3],[2,2,4]],[[2,5,67],[3,4,21]]])
print(d)
print("3d dimensional", d.ndim)

e=np.array([[3,4,6,3],[4,4,3,4]],ndmin=6)

print(e)
print(e.ndim)