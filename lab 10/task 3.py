import matplotlib.pyplot as plt

flavors = ['Vanilla', 'Chocolate', 'Strawberry', 'Mint Chocolatechip', 'Cookie Dough']
sales = [2134, 5634, 1222, 4343, 3231]

plt.pie(sales, labels=flavors)
plt.show()
