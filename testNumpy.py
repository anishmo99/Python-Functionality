import numpy as np
#array syntax
#np.array(object, dtype = None, copy = True, order = None, subok = False, ndmin = 0)

a=np.array([1,2,3,4,5])
print(a)
print(np.array(a,ndmin=2,dtype=complex)) # makes the array a 2D
