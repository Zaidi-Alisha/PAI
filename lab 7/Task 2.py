import numpy as np
mat = np.arange(1, 19,2).reshape(3,3)
print(mat)

count = 1
for i in mat:
    print(f"Row {count} : {i}") 
    count = count + 1