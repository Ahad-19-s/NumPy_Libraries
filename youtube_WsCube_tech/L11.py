import numpy as np

print("===== NumPy Indexing & Slicing Project: Data Explorer =====\n")

# Step 1: Create / Input Array
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

print(f"\nEnter {rows*cols} elements row-wise (space separated):")
elements = list(map(int, input().split()))

if len(elements) != rows * cols:
    print("❌ Error: Number of elements does not match rows x columns")
    exit()

arr = np.array(elements).reshape(rows, cols)

print("\n===== Your Array =====")
print(arr)
print("Shape:", arr.shape)

# Step 2: Row selection
row_idx = int(input("\nSelect a row index (0-based): "))
print(f"Row {row_idx}:", arr[row_idx, :])

# Step 3: Column selection
col_idx = int(input("\nSelect a column index (0-based): "))
print(f"Column {col_idx}:", arr[:, col_idx])

# Step 4: Submatrix selection
print("\nSelect submatrix:")
r_start = int(input("Row start index: "))
r_end   = int(input("Row end index (exclusive): "))
c_start = int(input("Column start index: "))
c_end   = int(input("Column end index (exclusive): "))

print("Submatrix:\n", arr[r_start:r_end, c_start:c_end])

# Step 5: Boolean indexing
cond = int(input("\nEnter a value to filter array elements greater than it: "))
print("Elements greater than", cond, ":", arr[arr > cond])

# Step 6: Step slicing
step = int(input("\nEnter step value for row slicing: "))
print(f"Rows with step {step}:\n", arr[::step, :])

# Step 7: Reverse array
rev_rows = arr[::-1, :]
rev_cols = arr[:, ::-1]
print("\nReversed Rows:\n", rev_rows)
print("Reversed Columns:\n", rev_cols)

print("\n===== Project Complete =====")
