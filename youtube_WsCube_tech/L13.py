import numpy as np

print("---- ORIGINAL ARRAY ----")
arr = np.array([1, 2, 3, 4, 5])
print("arr =", arr)

# -----------------------------------------------------------
# 1️⃣ VIEW (Shallow Copy)
# -----------------------------------------------------------
print("\n---- VIEW (SHALLOW COPY) ----")
view_arr = arr.view()

print("view_arr =", view_arr)

# Change in view affects original?
view_arr[0] = 100
print("\nAfter modifying view_arr[0] = 100")
print("arr =", arr)        # original changed
print("view_arr =", view_arr)

# Check memory location
print("\nMemory Address Check:")
print("arr.base ->", arr.base)
print("view_arr.base ->", view_arr.base)   # Points to original array


# -----------------------------------------------------------
# 2️⃣ COPY (Deep Copy)
# -----------------------------------------------------------
print("\n---- COPY (DEEP COPY) ----")
copy_arr = arr.copy()

print("copy_arr =", copy_arr)

# Change in copy DOES NOT affect original
copy_arr[1] = 999
print("\nAfter modifying copy_arr[1] = 999")
print("arr =", arr)        # original unchanged
print("copy_arr =", copy_arr)

# Memory Address
print("\nMemory Address Check:")
print("copy_arr.base ->", copy_arr.base)   # None means independent copy


# -----------------------------------------------------------
# 3️⃣ VIEW Example in 2D Array
# -----------------------------------------------------------
print("\n---- VIEW in 2D ARRAY ----")

arr2d = np.array([[10, 20, 30],
                  [40, 50, 60]])

view2d = arr2d.view()
view2d[0][1] = 888

print("arr2d =\n", arr2d)      # Original changed
print("view2d =\n", view2d)


# -----------------------------------------------------------
# 4️⃣ COPY Example in 2D Array
# -----------------------------------------------------------
print("\n---- COPY in 2D ARRAY ----")

copy2d = arr2d.copy()
copy2d[1][2] = 777

print("arr2d =\n", arr2d)      # Original NOT changed
print("copy2d =\n", copy2d)
