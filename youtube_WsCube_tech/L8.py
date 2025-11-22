import numpy as np

print("===== NumPy Arithmetic Calculator =====")

# User input for first array
a = list(map(int, input("Enter first list of numbers (space separated): ").split()))
b = list(map(int, input("Enter second list of numbers (space separated): ").split()))

# Convert to numpy arrays
arr1 = np.array(a)
arr2 = np.array(b)

print("\n===== Results =====")

print("Array 1 =", arr1)
print("Array 2 =", arr2)

# Arithmetic operations
print("\nAddition:", np.add(arr1, arr2))
print("Subtraction:", np.subtract(arr1, arr2))
print("Multiplication:", np.multiply(arr1, arr2))
print("Division:", np.divide(arr1, arr2))
print("Power (arr1^2):", np.power(arr1, 2))
print("Modulus:", np.mod(arr1, arr2))
print("Floor Division:", np.floor_divide(arr1, arr2))
print("Square Root of arr1:", np.sqrt(arr1))
print("Log of arr1:", np.log(arr1))
print("Exponential of arr1:", np.exp(arr1))

print("\n===== Program Finished =====")
