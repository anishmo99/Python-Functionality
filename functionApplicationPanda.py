import pandas as pd
import numpy as np


def adder(ele1, ele2):
    return ele1 + ele2


d = {'col1': pd.Series([1, 2, 3, 4, 5]),
     'col2': pd.Series([2, 4, 6, 8, 10]),
     'col3': pd.Series([3, 6, 9, 12, 15])}
df = pd.DataFrame(d)
print(df)
df = df.pipe(adder, 2)  # adding each number with 2 using the added function
print(df)
print(df.apply(np.mean))  # can also be written as -> print(df.mean())

# row&column wise function application

df['col1'] = df['col1'].map(lambda x: x * 100)  # for each element x present in the df column1
df['col2'] = df['col2'].map(lambda y: y * 2)  # column2
df['col3'] = df['col3'].map(lambda z: z + 3)
print(df)
print(df.apply(np.mean))

# iloc is used as row and column selector

print(df.iloc[2])  # prints the 2nd row
print(df.iloc[:, 2])  # prints the 2nd column
print(df.iloc[3, 2])  # prints the element in the 3rd row and 2nd column
