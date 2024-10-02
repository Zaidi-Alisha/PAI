import pandas as pd
import numpy as np

data = pd.read_csv(r"C:\Users\k230025\Desktop\task\heart (1).csv")

a = data[data['ca'] == 2]
b = data[data['ca'] == 0]
c = data[data['ca'] == 1]

print(a.mean())
print(b.mean())
print(c.mean())

'''Filtering can be done by:
"Single group,single column", "Single group, multiple column",
"Multiple group, single column", "Multiple group, multiple column"'''

data.rename(columns={'sex' : 'gender'}, inplace=True)

data['gender'] = data['gender'].replace({0: 'F', 1: 'M'})
print(data.head())

male_records = data[data['gender'] == 'M']
female_records = data[data['gender'] == 'F']

print("Male records: ", male_records)
print("Female records: ", female_records)


df = data.groupby('gender')

#Single group
print(df['chol'].max(), end='\n\n')
print(df['chol'].mean(), end='\n\n')
print(df['chol'].median(), end='\n\n')


#Multiple group
print(df[['restecg', 'oldpeak', 'chol']].max(), end='\n\n')
print(df[['restecg', 'oldpeak', 'chol']].mean(), end='\n\n')
print(df[['restecg', 'oldpeak', 'chol']].median(), end='\n\n')

'''Concat Data'''
Data1 = {
    'Name': ["Alisha", "Sarim", "Amna"],
    'Age': [17, 15, 19]
}

Data2 = {
    'Gender': ["Female", "Male", "Female"],
    'Marks': [23, 21, 22]
}

df1 = pd.DataFrame(Data1)
df2 = pd.DataFrame(Data2)

axis0 = pd.concat([df1, df2], axis=0)

axis0.index = ['0', '1', '2', '3', '4', '5']

print("Concatenated along axis 0:")
print(axis0)

axis1 = pd.concat([df1, df2], axis=1)

axis1.index = ['0', '1', '2']

print("\nConcatenated along axis 1:")
print(axis1)

iris_data = pd.read_csv(r"C:\Users\k230025\Desktop\task\iris.csv")
print(iris_data.isnull().sum())
print(iris_data.fillna(45, inplace=True))
