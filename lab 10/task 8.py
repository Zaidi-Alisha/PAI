import matplotlib.pyplot as plt
import numpy as np
x = np.arange(1, 11)
y1 = x ** 2  # Example metric 1
y2 = x ** 1.5  # Example metric 2

plt.figure(figsize=(10, 6))
plt.plot(x, y1, color='pink', marker='o', label='y1 = x^2')
plt.plot(x, y2, color='gray', marker='o', label='y2 = x^1.5')

plt.title('Two Lines on One Graph')
plt.xlabel('Amazing X-axis')
plt.ylabel('Incredible Y-axis')
plt.legend(loc='lower right')
plt.grid()
plt.show()
