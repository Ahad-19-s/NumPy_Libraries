# import numpy as np
# arr=np.array([1,2,3,4,5])
# print(type (arr))
# print(arr+2)
import numpy as np
import time

# List
lst = [i for i in range(1000000)]
start = time.time()
lst2 = [x * 2 for x in lst]
print("List time:", time.time() - start)

# NumPy Array
arr = np.array(lst)
start = time.time()
arr2 = arr * 2
print("Array time:", time.time() - start)
