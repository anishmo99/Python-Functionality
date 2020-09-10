import pandas as pd
import numpy as np

d = {'col1': pd.Series([1, 2, 3, 4, 5]),
     'col2': pd.Series([2, 4, 6, 8, 10]),
     'col3': pd.Series([3, 6, 9, 12, 15])}
d2 = {'col1': pd.Series([10, 20, 30, 40]),
      'col2': pd.Series([20, 40, 60, 80]),
      'col3': pd.Series([30, 60, 90, 120])}

df = pd.DataFrame(d)
df2 = pd.DataFrame(d2)

df2 = df2.reindex_like(df)  # elements remain the same, but the layout changes // df2's layout looks like df

print(df2)
