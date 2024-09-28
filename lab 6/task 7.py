import pandas as pd

df = pd.read_excel('employee.xlsx')

specified_year = 2018  

df_filtered = df[df['Year'] == specified_year]

print("List of employees from the year ", specified_year)
print(df_filtered)
