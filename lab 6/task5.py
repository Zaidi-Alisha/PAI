import pandas as pd

df = pd.read_csv(r'C:\Users\k230025\Desktop\task\Book1.csv')
data_head = df.head()

print(data_head)


loaded_data = load_from_json()
find_max(loaded_data)
