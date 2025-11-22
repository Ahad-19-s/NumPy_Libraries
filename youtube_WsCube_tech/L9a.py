import numpy as np

print("===== NumPy Shape & Reshape Analyzer Project =====\n")

# Step 1: User Input Array
user_input = list(map(float, input("Enter numbers (space separated): ").split()))
arr = np.array(user_input)

print("\n===== ORIGINAL ARRAY INFO =====")
print("Array:", arr)
print("Shape:", arr.shape)
print("Dimensions (ndim):", arr.ndim)
print("Total Elements:", arr.size)

# Step 2: Auto Reshape Suggestions
print("\n===== POSSIBLE RESHAPE OPTIONS =====")
n = arr.size

# find possible reshape pairs (rows, cols)
pairs = [(i, n//i) for i in range(1, n+1) if n % i == 0]

print("You can reshape into:")
for r, c in pairs:
    print(f"  → {r} x {c}")

# Step 3: Flatten Array
print("\n===== FLATTENED ARRAY =====")
print(arr.flatten())

# Step 4: ML-Friendly reshape
print("\n===== ML FRIENDLY RESHAPE (n,1) =====")
ml_shape = arr.reshape(-1, 1)
print(ml_shape)

# Step 5: User Custom Reshape
print("\n===== CUSTOM RESHAPE =====")
try:
    r = int(input("Enter rows: "))
    c = int(input("Enter columns: "))

    print("\nReshaped Array:")
    print(arr.reshape(r, c))
except Exception as e:
    print("❌ Error:", e)
    print("Reason: Total elements must remain same!")

print("\n===== PROJECT COMPLETE =====")
