import pandas as pd

df_alcohol = pd.read_csv(r'C:\Users\k230025\Desktop\task\Book1.csv')

alcohol_consumption = df_alcohol[df_alcohol['Year'].isin([1987, 1989])]

print(alcohol_consumption)

