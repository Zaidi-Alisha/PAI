import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv(r"C:\Users\Yousuf Traders\Desktop\PAI\heart.csv")
df = data.corr()

plt.figure(figsize=(11, 9))
heat_map = sns.heatmap(data=df, annot=True, fmt=".2f", cmap='Purples', square=True, cbar=True)
plt.title('Heatmap')
plt.show()

'''For histogram'''
histoplot =sns.histplot(data= data, x ="age", bins=30)
plt.title("Trestbps V/s Age")
plt.show() 
