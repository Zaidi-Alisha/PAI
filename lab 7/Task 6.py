import numpy as np
mat_5x3 = np.random.randint(1, 100, size=(5, 3))
print("Matrix of order 5x3")
print(mat_5x3)
mat_3x2 = np.random.randint(1, 100, size=(3, 2))
print("Matrix of order 3x2")
print(mat_3x2)
result = np.dot(mat_5x3, mat_3x2)
print("Multiplied matrix")
print(result)