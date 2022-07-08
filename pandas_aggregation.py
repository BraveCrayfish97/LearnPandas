import pandas as pd
df = pd.read_csv('pokemon_datav2.csv')

#gets the mean of any stat and ouputs the least and greated of them

inp = input("What stat would u like t group by?\n>")

mean_df = df.groupby(['Type 1']).mean()

print(mean_df.sort_values(inp))
temp_df = mean_df.sort_values(inp)[inp]
print(temp_df)
print(str(temp_df.head(1)))
print(temp_df.tail(1))

