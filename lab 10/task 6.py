import matplotlib.pyplot as plt

math = [87, 78, 76, 77, 98, 76, 88, 89, 91, 92]
science = [84, 88, 91, 77, 93, 74, 83, 78, 98, 93]

plt.scatter(math, science, color='green')
plt.xlabel('Mathematics Marks')
plt.ylabel('Science Marks')
plt.title('Mathematics and Science Marks')
plt.legend()
plt.show()
