import pandas as pd

stuff = {
    "first":['Rishi', 'Krishina', "Chaitu"],
    "last": ['Chapati', 'Chapati', 'Chapati'],
    'city':["Dallas", "Dallas", "Dallas"]
}
df = pd.DataFrame(stuff)

print(df)
df.to_csv('pandas_family.csv')