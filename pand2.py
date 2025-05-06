import pandas as pd

df1 = pd.DataFrame({
    "key": list("abcdefgh"),
    "value": [11, 22, 33, 44, 55, 66, 77, 88]
})
# print(df1)

df2 = pd.DataFrame({
    "key": list("ajclmnop"),
    "value": [99, 88, 77, 66, 55, 44, 33, 22]
})
# print(df2)

# print(pd.concat((df1,df2)))

## MERGE

print(pd.merge(df1,df2, on="key"))