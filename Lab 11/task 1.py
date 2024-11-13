import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

heart_data = pd.read_csv(r'C:\Users\k230025\Desktop\PAI\heart.csv')

X = heart_data.drop(columns=['target'])
y = heart_data['target']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

k_values = range(1, 251)
accuracies = []

for k in k_values:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    accuracies.append(accuracy)

maximum = max(accuracies)
minimum = min(accuracies)
best = [k for k, acc in zip(k_values, accuracies) if acc == maximum]
worst = [k for k, acc in zip(k_values, accuracies) if acc == minimum]

# Display the results
print("Highest Accuracy:", maximum)
print("Best k value(s):", best)
print("Lowest Accuracy:", minimum)
print("Worst k value(s):", worst)
