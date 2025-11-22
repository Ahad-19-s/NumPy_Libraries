import numpy as np

print("\n==============================")
print("      UNIQUE FUNCTION")
print("==============================")

arr1 = np.array([13, 23, 23, 333, 344, 333])
u, c = np.unique(arr1, return_counts=True)
print("Unique values:", u)
print("Counts:", c)


print("\n==============================")
print("         RESIZE")
print("==============================")

arr2 = np.array([1, 2, 3])
resized = np.resize(arr2, (2, 4))
print("Original:", arr2)
print("Resized array:\n", resized)


print("\n==============================")
print("     FLATTEN vs RAVEL")
print("==============================")

arr3 = np.array([[10, 20], [30, 40]])

flat = arr3.flatten()
rav = arr3.ravel()

print("Original:\n", arr3)
print("Flatten (copy):", flat)
print("Ravel (view):", rav)

# prove ravel is view
arr3[0, 0] = 999
print("After changing arr3:")
print("Ravel updates automatically:", rav)


print("\n==============================")
print("          SHUFFLE")
print("==============================")

arr4 = np.array([100, 200, 300, 400, 500])
print("Before shuffle:", arr4)

np.random.shuffle(arr4)
print("After shuffle:", arr4)
