import pandas as pd

data = {
    'ages': [14, 18, 24, 42],
    'heights': [165, 180, 176, 184]
}

df = pd.DataFrame(data, index=['James', 'Bob', 'Amy', 'Dave'])
print(df)
