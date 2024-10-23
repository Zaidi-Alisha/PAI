import matplotlib.pyplot as plt
import pandas as pd
df= pd.read_csv("iris.csv")
x = df['sepal_length']
y = df['petal_width']

filtered_data = df[df['species'].isin(['setosa', 'versicolor'])]
species_count = filtered_data['species'].value_counts()
plt.figure(figsize=(8, 5))
plt.bar(species_count.index, species_count.values, color=['green', 'yellow'])
plt.title('Count of setosa and versicolor')
plt.xlabel('species')
plt.ylabel('Count')
'''Rotatate axis'''
plt.xticks(rotation=0)  

plt.grid(axis='y')
print("v:", species_count)
plt.show()
