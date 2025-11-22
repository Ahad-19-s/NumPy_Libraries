import numpy as np

print("===== MATRIX CREATION =====")
A = np.matrix([[1, 2, 3],
               [4, 5, 6]])
B = np.matrix([[7, 8, 9],
               [1, 2, 3]])

print("Matrix A:\n", A)
print("Matrix B:\n", B)

# Shape
print("\nShape of A:", A.shape)
print("Shape of B:", B.shape)

print("\n===== MATRIX OPERATIONS =====")

# Matrix Addition
print("\nAddition (A + B):\n", A + B)

# Matrix Subtraction
print("\nSubtraction (A - B):\n", A - B)

# Elementwise Multiplication
print("\nElement-wise Multiplication (A * B):\n", np.multiply(A, B))

# Matrix Multiplication
print("\nMatrix Multiplication (A dot B.T):\n", A * B.T)

print("\n===== MATRIX TRANSFORMATIONS =====")

# Transpose
print("\nTranspose of A:\n", A.T)

# Matrix inverse (square matrix needed)
C = np.matrix([[4, 7],
               [2, 6]])

print("\nMatrix C:\n", C)
print("\nInverse of C:\n", np.linalg.inv(C))

# Determinant
print("\nDeterminant of C:", np.linalg.det(C))

# Rank
print("\nRank of A:", np.linalg.matrix_rank(A))

print("\n===== MATRIX STACKING =====")

# Vertical Stack
print("\nVertical Stack:\n", np.vstack([A, B]))

# Horizontal Stack
print("\nHorizontal Stack:\n", np.hstack([A, B]))

print("\n===== MATRIX FLATTENING =====")

# Flatten Matrix
print("\nFlatten A:\n", A.flatten())

# Ravel (view)
print("\nRavel A:\n", np.ravel(A))

print("\n===== RESHAPE MATRIX =====")

arr = np.array([1, 2, 3, 4, 5, 6])
print("\nOriginal Array:", arr)

print("Reshaped to 3x2:\n", arr.reshape(3, 2))

print("\n===== END =====")
