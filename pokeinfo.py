import pandas as pd

df = pd.read_csv('pokemon_datav2.csv')

pokemon = input("Enter ur pokemon>")
stat_inp = input("Enter ur stats>").split(' ')

def all_stats(name):
    print(df.loc[df['Name'] == name])
def stat(s, name):
    try:
        temp_df = df.loc[df['Name'] == name]
        val = int(temp_df[str(s)])
        print(f"{name} {s}: {val}")
    except:
        print("please enter the correct name/stat")

for i in stat_inp:
    stat(i, pokemon)
    #print(int(temp_df[str(i)]))

