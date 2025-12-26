import numpy as np

# 0 dimansional 
a= np.array(23)
print(a)

# 1d 
b= np.array([32,35,56,6])

print(b[0] + b[2])


arr = np.array([[1,2,3,4,5],
                 [6,7,8,9,10]])

print('2nd element on 2st row: ', arr[1, 1])


arr = np.array([[[1, 2, 3], [4, 5, 6]],
                 [[7, 8,7], [10, 11, 12]]])

print(arr[1, 1, 2])