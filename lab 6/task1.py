import pandas as pd

data = {
    'title': ['Harry Potter and the Prisoner of Azkaban', 'Interstellar', 'The Notebook', 'Home Alone 3'],
    'revenue': [2345678, 567890, 340909098, 3456789],
    'spent': [890678, 2345679, 456789, 6789087]
}

df = pd.DataFrame(data)

filter = df[(df['revenue'] > 2000000) & (df['spent'] < 1000000)]
print(filter)
