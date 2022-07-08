import pandas as pd

#reads from csv
df = pd.read_csv("D:\PandasPython\pokemon_data.csv")

#gets first & last 3 rows
#print(df.head())
#print(df.tail())

#gets all columns of the table
#print(df.columns)

#gets name of all pokemon
#print(df["Name"])

#gets name of top 5 pokemon
#print(df["Name"][0:5])

#gets only first 3 columns and first 5 rows
#print(df[df.columns[0:3]][0:5])

#gets rows 1-4
#print(df.iloc[1:4])

#gets a specific value
#print(df.iloc[2, 1])

#iterate through each row and prints the names or whatever
#for index, row in df.iterrows():
#    print(index, row["Name"])

#gets pokemon with highest stat
#lst = []
#for index, row in df.iterrows():
#    if row["Attack"] >= 100:
#        print(index, row[["Name", "HP", "Attack", "Defense", "Sp. Atk", "Sp. Def", "Speed"]])
#        total = row["HP"]+row["Attack"]+row["Defense"]+row["Sp. Atk"]+row["Sp. Def"]+row["Speed"]
#        lst.append([row["Name"], total])
#temp = []
#for i in lst:
#    temp.append(i[1])
#most_hp = max(temp)
#for i in lst:
#    if i[1]==most_hp:
#        print(f"{i[0]} has {most_hp} stats")

    

#loc gets data through textual queries
#print(df.loc[df['Type 1']=="Fire"])
#print(df.loc[df['Legendary']==True])
#print(df.loc[df['Name'] == "RayquazaMega Rayquaza"])

#descibe gets mean, median, standard deviarion etc.
#print(df.describe())

#sort by specific value ascending or descending
#print(df.sort_values('HP', ascending=False))
#print(df.sort_values(['Type 1', 'HP'], ascending = [0, 0]))


#adding a "Total" column
#df['Total'] = df['HP']+df['Attack']+df['Defense']+df['Sp. Atk']+df['Sp. Def']+df['Speed']

#better way
df['Total'] = df.iloc[:, 4:10].sum(axis = 1)
#^^new col 'Total'   ^: for all rows and 4:9 for 4th through 9th column|axis 1 is saying to add horizontally


#deleting columns
#df = df.drop(columns = ['Generation', "Legendary"])

#reorganizing cols
cols = list(df.columns.values)

df = df[cols[0:4] + [cols[-1]] + cols[4:12]]
#print(df.head())
df.to_csv('pokemon_datav2.csv', index=False)
