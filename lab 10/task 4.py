import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('students.csv')

age_bins = [18, 25, 30, 35, float('inf')]
labels = ['18-25', '26-30', '31-35', '36 and above']
data['Age Group'] = pd.cut(data['Age'], bins=age_bins, labels=labels, right=False)

distribution = data['Age Group'].value_counts()

plt.pie(distribution, labels=distribution.index)
plt.title('Age Distribution')
plt.show()
