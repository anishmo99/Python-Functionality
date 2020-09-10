import pandas as pd
import numpy as np

d = np.random.randn(10, 2)
df = pd.DataFrame(d, index=[5, 4, 3, 6, 2, 7, 8, 9, 1, 10])
print(df)
df1 = df.sort_index()  # sorts the index in ascending order
print(df1)
df2 = df.sort_index(ascending=False)  # sorts the index in descending order
print(df2)
d1 = {'one': pd.Series([5, 3, 4, 1, 2]),
      'two': pd.Series([20, 10, 30, 50, 40])}
df3 = pd.DataFrame(d1)
print(df3)
df3 = df3.sort_values(by='one',
                      kind='mergesort')  # heapsort, quicksort also available. mergesort is the only stable algorithm
print(df3)
