import pandas as pd
#df = pd.read_csv('pokemon_datav2.csv')

#print(df.applymap(str).head().applymap(len).head())

#finds pokemon with the longest name
##longest_name = max(list(df['Name'].apply(len)))
#indx = list(df['Name'].apply(len)).index(longest_name)
#print(df.loc[indx])

#making mega pokemon names look nicer
#def removeMega(name):
#    if 'Mega' in name:
#        lst = name.split('Mega')
#
#        return "Mega" + lst[1]
#    else:
#        return name
#print(df['Name'].apply(removeMega))
#filt = df['Legendary'] == False
#print(df.drop(index = df[filt].index))
    