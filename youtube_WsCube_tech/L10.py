import numpy as np

print("===== Broadcasting Project =====")

A = np.array([[1,2,3], [4,5,6]])
B = np.array([10,20,30])
C = np.array([[100], [200]])

print("A + B =")
print(A + B)

print("A + C =")
print(A + C)

print("Shape of A:", A.shape)
print("Shape of B:", B.shape)
print("Shape of C:", C.shape)
