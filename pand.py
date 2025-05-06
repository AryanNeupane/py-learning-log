import pandas as pd

s=pd.Series([1,2,4,6,8])
# print(s)

# si=pd.Series([1,2,4,6,8],['a','s','d','f','g'])
# print(si)

df=pd.read_csv("day.csv")
# print(df)
# print(df.head())
# print(df.tail())
# print(df.describe())
# print(df.info())

# print(df['Numeric'])

# print(df.iloc[0])

df2=pd.read_csv("day2.csv")

print(df2.head(10))

# print(df2.dropna())
print(df2.fillna(0))
# print(df2.head(10))

