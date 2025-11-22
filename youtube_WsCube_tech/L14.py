import numpy as np

print("\n==============================")
print("   JOINING NUMPY ARRAYS")
print("==============================")

# ---------------------------------------------------------
# 1️⃣ Using concatenate()
# ---------------------------------------------------------
print("\n---- 1. CONCATENATE ----")

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

result_concat = np.concatenate((arr1, arr2))
print("arr1:", arr1)
print("arr2:", arr2)
print("concatenate:", result_concat)

# 2D concatenate
arr3 = np.array([[10, 20], [30, 40]])
arr4 = np.array([[50, 60], [70, 80]])

result_concat_2d = np.concatenate((arr3, arr4), axis=0)
print("\n2D concatenate axis=0:\n", result_concat_2d)

result_concat_2d_axis1 = np.concatenate((arr3, arr4), axis=1)
print("\n2D concatenate axis=1:\n", result_concat_2d_axis1)



# ---------------------------------------------------------
# 2️⃣ Using stack()
# ---------------------------------------------------------
print("\n---- 2. STACK ----")

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

v_stack = np.vstack((a, b))
print("\nVertical Stack (vstack):\n", v_stack)

h_stack = np.hstack((a, b))
print("\nHorizontal Stack (hstack):\n", h_stack)

d_stack = np.dstack((a, b))
print("\nDepth Stack (dstack):\n", d_stack)

# Generic stack
generic_stack = np.stack((a, b), axis=0)
print("\nGeneric stack axis=0:\n", generic_stack)

generic_stack_axis1 = np.stack((a, b), axis=1)
print("\nGeneric stack axis=1:\n", generic_stack_axis1)



print("\n==============================")
print("     SPLITTING NUMPY ARRAYS")
print("==============================")

# ---------------------------------------------------------
# 3️⃣ Using array_split()
# ---------------------------------------------------------
print("\n---- 3. ARRAY_SPLIT ----")

arr = np.array([10, 20, 30, 40, 50, 60, 70])

split_result = np.array_split(arr, 3)
print("Original array:", arr)
print("Split into 3 parts:", split_result)

# Each part
for i, part in enumerate(split_result):
    print(f"Part {i+1}:", part)


# 2D split
arr2d = np.array([[1, 2, 3, 4],
                  [5, 6, 7, 8]])

row_split = np.array_split(arr2d, 2, axis=0)
print("\n2D Split axis=0:", row_split)

col_split = np.array_split(arr2d, 2, axis=1)
print("\n2D Split axis=1:", col_split)
