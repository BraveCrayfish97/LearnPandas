import pandas as pd

df = pd.read_csv('pokemon_datav2.csv')

#makes all fire pokemon have type 2 as water
#df.loc[df['Type 1']=='Fire', "Type 2"] = "Water"
#     ^query for fire pokemon ^we want to change Type 2 to Water

