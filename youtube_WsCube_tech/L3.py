import numpy as np

a= np.array(["ahad","sabina","shipon","sadid"])
print(a)

import numpy as np

# Input নেওয়া
lst = []
for i in range(1, 5):
    s = int(input("Enter a number: "))  # int() করে নিচ্ছি
    lst.append(s)

# List থেকে array বানানো
x = np.array([lst],[1,2,3])

# Operation করা
print("Original Array:", x)
print("After x*2 + 2:", x * 2 + 2)
print(x.ndim)
