import pandas as pd
import numpy as np

#series
'''
s = pd.Series(np.random.randn(5))
print(s)
print (s.tail(2))
'''
#dataFrame
d={'name':['anish','harshal','shivam','joyal'],
    'age':[20,20,19,19],
    'home':['kol','mum','del','ker'],
   'rate':[4.4,4.3,5.4,6.5],
   'rate2':[1,2,3,4]}
pf=pd.DataFrame(d,index=[1,2,3,4])
print(pf.T) #transpose//opposite
print(pf.axes)
print(pf.dtypes)
print(pf.empty)
print(pf.ndim)
print(pf.shape)
print(pf.size)
print(pf.head(2))
print(pf.sum()) #appends everything // adds sidewise // individual column is added
print(pf.sum(1)) #adds only the no.s
print(pf.mean()) #mean of all numerical datas
print(pf.std()) # standard deviation
print(pf.describe()) #all statistical datas provided
print(pf.describe(include='all')) #all including objects
print(pf.describe(include='object')) #only objects
