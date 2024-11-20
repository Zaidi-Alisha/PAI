from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv(r'C:\Users\k230025\Desktop\PAI\iris.csv')
X = df[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']]

wcss = []
k_values = range(1, 11)  

for k in k_values:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)  

plt.figure(figsize=(8, 6))
plt.plot(k_values, wcss, marker='o', linestyle='--', color='b')
plt.title('Elbow Method for Optimal Clusters')
plt.xlabel('Number of Clusters (k)')
plt.ylabel('Within-Cluster Sum of Squares (WCSS)')
plt.xticks(k_values)
plt.grid()
plt.show()
