import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv(r'C:\Users\Yousuf Traders\Desktop\PAI\cement_slump.csv')

sns.set(style="whitegrid")

plt.figure(figsize=(10, 8))
for i, col in enumerate(data.columns, 1):
    plt.subplot(2, 5, i)
    sns.boxplot(y=data[col])
    plt.title(f'Boxplot of {col}')
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 8))
for i, col in enumerate(data.columns, 1):
    plt.subplot(2, 5, i)
    sns.histplot(data[col], kde=True)
    plt.title(f'Distribution of {col}')
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 8))
mat = data.corr()
sns.heatmap(mat, annot=True, cmap="coolwarm", fmt=".2f", vmin=-1, vmax=1)
plt.title('Correlation Matrix')
plt.show()

pairs = [(col1, col2) for col1 in mat.columns for col2 in mat.columns 
                   if abs(mat.loc[col1, col2]) > 0.6 and col1 != col2]

plt.figure(figsize=(15, 8))
for i, (col1, col2) in enumerate(pairs[:6], 1):  
    plt.subplot(2, 3, i)
    sns.scatterplot(data=data, x=col1, y=col2, alpha=0.7)
    sns.regplot(data=data, x=col1, y=col2, scatter=False, color="red")
    plt.title(f'Relationship between {col1} and {col2}')
plt.tight_layout()
plt.show()
