import pandas as pd

df = pd.read_csv('pokemon_datav2.csv')
#Filtering wil loc----------------------------------
#making new df with only grass&posion pokemon
#new_df = df.loc[(df['Type 1']=='Grass')&(df['Type 2']=='Poison')]

#reseting the index back to normal
#print(new_df.reset_index(drop=True))

#only mega pokemon
#print(df.loc[df['Name'].str.contains('Mega')])

#only non_mega pokemon
#print(df.loc[~df['Name'].str.contains('Mega')])
