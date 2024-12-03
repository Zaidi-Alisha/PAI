from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

#KNN
# Define features (X) and target (y)
X = cement_slump_data.drop(columns=['Compressive Strength (28-day)(Mpa)'])
y = (cement_slump_data['Compressive Strength (28-day)(Mpa)'] > 30).astype(int)  # Binary target for classification

# Train-test split with random state
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train KNN model
knn = KNeighborsClassifier(n_neighbors=5)  # n_neighbors can be tuned
knn.fit(X_train, y_train)

# Evaluate performance
y_pred = knn.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))


#Kmeans, PCA
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

# Use only numeric features
X = cement_slump_data.drop(columns=['Compressive Strength (28-day)(Mpa)'])

# KMeans clustering with n_clusters
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(X)

# Add cluster labels to the dataset
cement_slump_data['Cluster'] = kmeans.labels_

# Visualize clusters using PCA
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

plt.scatter(X_pca[:, 0], X_pca[:, 1], c=kmeans.labels_, cmap='viridis', alpha=0.6)
plt.title("KMeans Clusters")
plt.xlabel("PCA Component 1")
plt.ylabel("PCA Component 2")
plt.show()

#Random state in train split test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

#n-clusters
distortions = []
for i in range(1, 11):
    km = KMeans(n_clusters=i, random_state=42)
    km.fit(X)
    distortions.append(km.inertia_)

plt.plot(range(1, 11), distortions, marker='o')
plt.title("Elbow Method for Optimal Clusters")
plt.xlabel("Number of clusters")
plt.ylabel("Inertia")
plt.show()

#n-neighbors
for k in range(1, 11):
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    print(f"Accuracy with k={k}: {knn.score(X_test, y_test):.2f}")

#Evaluation metrics
#Accuracy score
print("Accuracy:", accuracy_score(y_test, y_pred))

#Confusion matrix and derived metrics
cm = confusion_matrix(y_test, y_pred)
tp = cm[1, 1]
tn = cm[0, 0]
fp = cm[0, 1]
fn = cm[1, 0]

print("Confusion Matrix:\n", cm)
print(f"TP: {tp}, TN: {tn}, FP: {fp}, FN: {fn}")

#Precision, Recall, and F1-Score:
from sklearn.metrics import precision_score, recall_score, f1_score

precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

print(f"Precision: {precision:.2f}, Recall: {recall:.2f}, F1-Score: {f1:.2f}")

#Classification Report
print("\nClassification Report:\n", classification_report(y_test, y_pred))

#Training and Testing Accuracy
train_accuracy = knn.score(X_train, y_train)
test_accuracy = knn.score(X_test, y_test)

print(f"Training Accuracy: {train_accuracy:.2f}")
print(f"Testing Accuracy: {test_accuracy:.2f}")


