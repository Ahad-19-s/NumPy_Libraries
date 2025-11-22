import numpy as np

print("===== Advanced NumPy Math Project =====")

# User input
a = list(map(float, input("Enter numbers (space separated): ").split()))
arr = np.array(a)

print("\n===== Input Array =====")
print("Array:", arr)

print("\n===== Arithmetic Functions =====")
print("Sum:", np.sum(arr))
print("Product:", np.prod(arr))
print("Minimum:", np.min(arr))
print("Maximum:", np.max(arr))
print("Mean:", np.mean(arr))
print("Median:", np.median(arr))
print("Standard Deviation:", np.std(arr))
print("Variance:", np.var(arr))

print("\n===== Trigonometric Functions (in radians) =====")
print("sin(x):", np.sin(arr))
print("cos(x):", np.cos(arr))
print("tan(x):", np.tan(arr))

print("\n===== Exponential / Log / Power =====")
print("exp(x):", np.exp(arr))
print("log(x):", np.log(arr))        # natural log
print("log10(x):", np.log10(arr))
print("Square Root:", np.sqrt(arr))
print("a^2:", np.power(arr, 2))

print("\n===== Rounding Functions =====")
print("Rounded:", np.round(arr))
print("Floor:", np.floor(arr))
print("Ceil:", np.ceil(arr))

print("\n===== Program Finished =====")
