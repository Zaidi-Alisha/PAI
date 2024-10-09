import numpy as np
mat = np.arange(2, 20, 2).reshape(3,3)
multiply = mat * 4
identity = np.eye(3)
result = np.dot(mat, multiply)
print(result)