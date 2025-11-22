import numpy as np

print("===== NumPy Iteration Tutorial Project =====\n")

# --------------------------- #
# 1. 1D Array Iteration
# --------------------------- #
arr1d = np.array([10, 20, 30, 40, 50])
print("1D Array:", arr1d)

print("\n1D Iteration (normal for loop):")
for x in arr1d:
    print(x, end=' ')
print()

# --------------------------- #
# 2. 2D Array Iteration
# --------------------------- #
arr2d = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])
print("\n2D Array:\n", arr2d)

print("\n2D Row-wise Iteration:")
for row in arr2d:
    print(row)

print("\n2D Element-wise Iteration (nested loop):")
for row in arr2d:
    for elem in row:
        print(elem, end=' ')
print()

print("\n2D Element-wise Iteration using nditer():")
for x in np.nditer(arr2d):
    print(x, end=' ')
print()

# --------------------------- #
# 3. 3D Array Iteration
# --------------------------- #
arr3d = np.arange(1, 13).reshape(2, 2, 3)
print("\n3D Array:\n", arr3d)

print("\n3D Element-wise Iteration using nditer():")
for x in np.nditer(arr3d):
    print(x, end=' ')
print()

print("\nIterating over first axis (2D slices):")
for x in arr3d:
    print(x)

# --------------------------- #
# 4. Modify Elements using nditer()
# --------------------------- #
arr_mod = np.array([1, 2, 3, 4])
print("\nOriginal Array for Modification:", arr_mod)

for x in np.nditer(arr_mod, op_flags=['readwrite']):
    x[...] = x * 2

print("Modified Array (doubled):", arr_mod)

# --------------------------- #
# 5. Iteration with Type Conversion
# --------------------------- #
arr_type = np.array([1, 2, 3, 4])
print("\nIteration with dtype conversion to float:")
for x in np.nditer(arr_type, flags=['buffered'], op_dtypes=['float']):
    print(x, type(x))

# --------------------------- #
# 6. Machine Learning Example: Feature Normalization
# --------------------------- #
features = np.array([[1, 2, 3],
                     [4, 5, 6]])
print("\nOriginal Features:\n", features)

for x in np.nditer(features, op_flags=['readwrite']):
    x[...] = (x - np.min(features)) / (np.max(features) - np.min(features))

print("Normalized Features:\n", features)

print("\n===== NumPy Iteration Tutorial Complete =====")
