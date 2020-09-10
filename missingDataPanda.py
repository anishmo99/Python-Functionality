import pandas as pd
import numpy as np

df=pd.DataFrame(np.random.randn(5,3),columns=['one','two','three'],index=['a','c','d','f','h'])
df=df.reindex(['a','b','c','d','e','f','g','h'])
print(df)
print(df['one'].isnull()) #checks if the value is Nan or not
print(df['one'].notnull()) #opposite of the above
#calculation with missing data
print("sum is ",df['one'].sum())
df=pd.DataFrame(index=[0,1,2,3,4,5],columns=['one','two'])
print("column1 sum is ",df['one'].sum()) #sum is either 0 or nan
#cleaning/filling data
df.fillna(0,inplace=True) #fills the nan with 0 values. written also as df=df.fillna(0)
print(df)
#Fill NA forward and backword
df=pd.DataFrame(np.random.rand(5,3),index=['a','c','e','f','h'],columns=['one','two','three'])
df=df.reindex(['a','b','c','d','e','f','g','h'])
print(df)
df.fillna(method='pad',inplace=True) #fills up nan values with data above. 'backfill' to fill nan values with below data
print(df)
df=pd.