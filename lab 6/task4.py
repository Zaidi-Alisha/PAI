import pandas as pd

data = {
    'name': ['Alisha','Layyana','Amna','Laiba'],
    'age': [23, 29, 13, 26]
}
df = pd.DataFrame(data)

change = [34, 35, 36, 37]

df.index = change
print("\nDataFrame with custom index:")
print(df)
