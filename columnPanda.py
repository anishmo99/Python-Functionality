import pandas as pd

d = {'one': pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd']),
     'two': pd.Series([2, 4, 6, 8], index=['a', 'b', 'c', 'd'])}
pf = pd.DataFrame(d)
print(pf)
print("\nNew column")
pf['three'] = pd.Series([3, 6, 9, 12], index=['a', 'b', 'c', 'd'])
print(pf)
pf['four'] = pf['one'] + pf['three']
print("\nNew column using pre existing columns")
print(pf)
print("\nDeleting column using POP")
pf.pop('two')
print(pf)
