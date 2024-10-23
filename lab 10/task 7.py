import matplotlib.pyplot as plt
# Sample data for sea level rise (year vs. height in mm)
years = np.arange(1920, 2021)
sea_levels = np.random.normal(loc=150, scale=10, size=len(years)).cumsum()  # Cumulative sum to simulate rise

plt.figure(figsize=(10, 6))
plt.scatter(years, sea_levels, color='blue', marker='o')
plt.title('Sea Level Rise Over 100 Years')
plt.xlabel('Year')
plt.ylabel('Sea Level (mm)')
plt.grid()
plt.show()
