import numpy as np

print("\n==============================")
print("      SEARCHING IN ARRAY")
print("==============================")

# ----------------------------------------
# 1️⃣ np.where() → search value positions
# ----------------------------------------
arr1 = np.array([10, 20, 30, 20, 50])
print("Array:", arr1)

pos = np.where(arr1 == 20)
print("Positions of value 20:", pos)


# ----------------------------------------------------
# 2️⃣ np.searchsorted() → insert position in sorted arr
# ----------------------------------------------------
sorted_base = np.array([10, 20, 30, 40])
insert_pos = np.searchsorted(sorted_base, 25)

print("\nSorted base array:", sorted_base)
print("Insert 25 at index:", insert_pos)



print("\n==============================")
print("  SORTED ARRAY (WITHOUT CHANGE)")
print("==============================")

# ----------------------------------------
# 3️⃣ np.sort() → original array unchanged
# ----------------------------------------
arr2 = np.array([40, 10, 50, 20])
sorted_arr = np.sort(arr2)

print("Original array:", arr2)
print("Sorted array:", sorted_arr)



print("\n==============================")
print("     SORT ARRAY (IN-PLACE)")
print("==============================")

# ----------------------------------------
# 4️⃣ arr.sort() → original array changed
# ----------------------------------------
arr3 = np.array([90, 10, 70, 20])
print("Before sort:", arr3)

arr3.sort()
print("After sort:", arr3)



print("\n==============================")
print("        FILTER ARRAY")
print("==============================")

# ----------------------------------------
# 5️⃣ Filter using Boolean mask
# ----------------------------------------
arr4 = np.array([10, 25, 30, 15, 50])
print("Original array:", arr4)

mask = arr4 > 20
print("Mask (values > 20):", mask)

filtered = arr4[mask]
print("Filtered array:", filtered)


# ----------------------------------------
# 6️⃣ One-line filter example
# ----------------------------------------
even_numbers = arr4[arr4 % 2 == 0]
print("\nEven numbers from array:", even_numbers)
