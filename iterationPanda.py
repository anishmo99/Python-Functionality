import pandas as pd
import numpy as np

d = np.random.randn(4, 4)
df = pd.DataFrame(d, columns=['col1', 'col2', 'col3', 'col4'], index=['a', 'b', 'c', 'd'])

print(df.iloc[3])
# iteration
print("column names")
for col in df:
    print(col)  # prints the column names
# iteritems
print("iteritems")
for key, value in df.iteritems():  # column wise (shows all the data under a column and then moves ahead)
    print(key, value)
print("iterrows")
for rkey, rvalue in df.iterrows():  # row wise (shows all the data in a single row and then moves ahead)
    print(rkey, rvalue)
# itertuples
print("itertuples")
for row in df.itertuples():  # row wise pura detail
    print(row)
# in iteration the values cant be altered. only meant for reading
