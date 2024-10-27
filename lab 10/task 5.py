import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('students.csv')

gender = data['Gender'].value_counts()

plt.pie(gender, labels=gender.index, autopct='%1.1f%%', startangle=140)
plt.title('Gender Distribution')
plt.show()
