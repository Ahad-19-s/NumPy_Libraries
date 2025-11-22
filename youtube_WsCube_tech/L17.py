import numpy as np

print("\n==============================")
print("         INSERT")
print("==============================")

arr = np.array([10, 20, 30, 40])
print("Original:", arr)

# Insert single value
insert1 = np.insert(arr, 2, 999)
print("Insert 999 at index 2:", insert1)

# Insert multiple values
insert2 = np.insert(arr, 1, [111, 222])
print("Insert multiple at index 1:", insert2)


print("\n---- 2D Insert ----")
arr2d = np.array([[1, 2], [3, 4]])
print("Original 2D:\n", arr2d)

# Insert row
ins_row = np.insert(arr2d, 1, [9, 9], axis=0)
print("Insert row at index 1:\n", ins_row)

# Insert column
ins_col = np.insert(arr2d, 1, [7, 7], axis=1)
print("Insert column at index 1:\n", ins_col)


print("\n==============================")
print("         DELETE")
print("==============================")

arr3 = np.array([10, 20, 30, 40, 50])
print("Original:", arr3)

del1 = np.delete(arr3, 2)
print("Delete index 2:", del1)

del2 = np.delete(arr3, [1, 3])
print("Delete multiple indexes:", del2)


print("\n---- 2D Delete ----")
arr2d = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

del_row = np.delete(arr2d, 1, axis=0)
print("Delete row 1:\n", del_row)

del_col = np.delete(arr2d, 1, axis=1)
print("Delete column 1:\n", del_col)
