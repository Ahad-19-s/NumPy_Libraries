import numpy as np

arr = np.array([[1, 2, 3],
                [4, 5, 6]])

print(arr.shape)
arr = np.array([1, 2, 3, 4, 5, 6])

reshaped = arr.reshape(3, 2)
print(reshaped)