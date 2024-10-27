import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv('sea_level.csv')

plt.scatter(data['Year'], data['Sea Level'], color='teal', label='Sea Level Rise')
plt.xlabel('Year')
plt.ylabel('Sea Level (in mm)')
plt.title('Sea Level Rise Over the Past 100 Years')
plt.legend()
plt.show()
