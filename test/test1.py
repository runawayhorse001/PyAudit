from PyAudit.basics	import missing_rate, zero_rate

import pandas as pd

d = {'A': [1, 0, None, 3],
     'B': [1, 0, 0, 0],
     'C': ['a', None, 'c', 'd']}

# create DataFrame
df = pd.DataFrame(d)
print(missing_rate(df))
print(zero_rate(df))



# read df
df = pd.read_csv('Heart.csv')
print(df.head(5))

print(missing_rate(df))
print(zero_rate(df))

df_num = df[['Age', 'Ca']]




