import matplotlib.pyplot as plt
# Sample age data
ages = [22, 24, 25, 30, 28, 31, 19, 20, 35, 40, 29, 22, 23, 33, 34, 38]
age_groups = ['18-25', '26-30', '31-35', '36 and above']
age_distribution = [sum(1 for age in ages if 18 <= age <= 25),
                   sum(1 for age in ages if 26 <= age <= 30),
                   sum(1 for age in ages if 31 <= age <= 35),
                   sum(1 for age in ages if age >= 36)]

plt.figure(figsize=(7, 7))
plt.pie(age_distribution, labels=age_groups, autopct='%1.1f%%', startangle=140)
plt.title('Student Age Distribution')
plt.axis('equal')
plt.show()
