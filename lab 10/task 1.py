import matplotlib.pyplot as plt
import numpy as np

# Sample data
names = ["Alisha", "Amna", "Sara", "laiba", "maha", 'ali', "eshal", "ayesha", "maria", "maheen", "tehreem", "saleem", "umar", "mehak", "aqsa", "abdullah", "Layyana", "Rayyan", "aaliya", "Alina"]
heights = [5.7, 5.2, 5.6, 6.4, 6.2, 5.7, 5.1, 5, 5.8, 5.9, 5.1, 5.7, 5.2, 5.6, 6.4, 6.2, 5.17, 5.1, 5, 5.81]

# Bar Chart
plt.xlabel("Names", fontsize = 18)
plt.ylabel("Heights", fontsize = 18)
plt.title("Student Data", fontsize = 18)
colors = ['g', 'r', 'b', 'y', 'm', 'black', 'g', 'r', 'b', 'y', 'm', 'black', 'g', 'r', 'b', 'y', 'm', 'black', 'g', 'y']
plt.bar(names, heights, width = 0.5, color=colors)
plt.show()

plt.pie(heights, labels=names)
plt.show()
