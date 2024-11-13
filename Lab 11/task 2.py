import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

data = pd.read_csv(r'C:\Users\k230025\Desktop\PAI\heart.csv')

X = data.drop(columns=['target'])  
y = data['target']

seed_accuracies = {}

for seed in range(1, 11):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=seed)
    
    accuracies = []
    
    for k in range(1, 251):
        knn = KNeighborsClassifier(n_neighbors=k)
        knn.fit(X_train, y_train)
        
        y_pred = knn.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        accuracies.append(accuracy)
    
    seed_accuracies[seed] = accuracies

all_accuracies = [acc for accuracies in seed_accuracies.values() for acc in accuracies]
highest_accuracy = max(all_accuracies)
lowest_accuracy = min(all_accuracies)

print("Accuracies by seed and k value:")
for seed, accuracies in seed_accuracies.items():
    print(f"Seed {seed}: {accuracies}")

print("\nHighest accuracy across all seeds:", highest_accuracy)
print("Lowest accuracy across all seeds:", lowest_accuracy)
