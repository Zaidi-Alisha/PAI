import numpy as np
generate = np.random.choice([2, 5, 9, 10], size= (4,4))
identity = np.eye(4)
odd = np.arange(1, 32,2).reshape(4,4)

mat_mul = np.dot(generate, identity)
result = np.add(odd, mat_mul)
print("Multiplied matrix")
print(mat_mul)
print("Addition matrix")
print(result)