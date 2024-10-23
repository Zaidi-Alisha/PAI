import matplotlib.pyplot as plt
# Sample gender data
genders = ['Male'] * 12 + ['Female'] * 8  # 12 Male, 8 Female
gender_distribution = [genders.count('Male'), genders.count('Female')]

plt.figure(figsize=(7, 7))
plt.pie(gender_distribution, labels=['Male', 'Female'], autopct='%1.1f%%', startangle=140)
plt.title('Gender Distribution Among Students')
plt.axis('equal')
plt.show()
