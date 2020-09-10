import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(8, 4),
                  columns=['A', 'B', 'C', 'D'],
                  index=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
# using loc
# select all rows for a specific column
print(df.loc[:, 'A'])
# select all rows for multiple columns
print(df.loc[:, ['A', 'C']])
# select few rows for multiple columns
print(df.loc[['a', 'c', 'e', 'f', 'h'], ['A', 'C']])
# selecting range of rows for all columns
print(df.loc['a':'h'])
# for getting boolean values with a boolean array
print(df.loc['a':'h'] > 0)

# using iloc
# select all rows for a specific column
print(df.iloc[1:3])
# integer slicing
# df.iloc[rowSelection,columnSelection]
print(df.iloc[:4])
print(df.iloc[1:5, 2:4])  # can also be written as print(df.loc['b':'e','C':'D'])