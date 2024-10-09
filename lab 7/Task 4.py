import numpy as np

dtype = [('name', 'U20'), ('height', 'f4'), ('class', 'i4')]
student = np.array([
    ('Alisha', 5.7, 2),
    ('Amna', 5.4, 3),
    ('Charlie', 5.8, 2),
    ('Bob', 5.7, 1),
    ('Eve', 5.4, 2)
], dtype = dtype)

print(student)
data = np.sort(student, order = ['class', 'height'])
print("\nSorted: ")
print(data)