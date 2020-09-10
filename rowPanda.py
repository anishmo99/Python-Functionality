import pandas as pd

d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
   'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}

df = pd.DataFrame(d)
print (df.loc['c']) #search through specified index

print(df.iloc[2]) #search through index

print(df[0:4]) #row selection

#addition of rows

d = [[1, 2], [3, 4]]
d2 = [[5,6],[7,8]]
pf = pd.DataFrame(d, columns=['a','b'])
print(pf)
pf2 = pd.DataFrame(d2, columns=['a','b'])
pf = pf.append(pf2)

print(pf)
pf['c']=pf['a']+pf['b']
print(pf)
pf=pf.drop(1)
print(pf)