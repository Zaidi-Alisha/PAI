import matplotlib.pyplot as plt

cities = ['Beijing', 'London', 'Karachi', 'Peshawar']
population = [1234545, 245343, 354421, 154312]

plt.figure(figsize=(10, 6))
plt.barh(cities, population, color='green')
plt.title('City Population')
plt.xlabel('Population')
plt.ylabel('Cities')
plt.show()
