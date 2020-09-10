import pandas as pd
import numpy as np

s = pd.Series(['Anish Mookherjee', 'Harshal Garg', np.nan, 'Shivam', 'Joyal', 'Sarthak'])
print(s.str.lower())
print(s.str.upper())
print(s.str.len())  # length of each string
print(s.str.strip())  # good for nothing
print(s.str.split(' '))  # splits with the letter/phrase mentioned
print(s.str.cat())  # concatenates all the elements
print(s.str.cat(sep=','))  # concatenates all the elements present with a separator between them
print(s.str.get_dummies())  # random one-hot coded values
print(s.str.contains('ish'))  # checks whether the mention letter/phrase is present or not
print(s.str.replace('ish', 'hello'))
print(s.str.repeat(2))  # Repeats each element with specified number of times
print(s.str.startswith('An'))  # return true or false
print(s.str.endswith('l'))
print(s.str.find('e'))  # Returns the first position of the first occurrence of the pattern else -1
print(s.str.findall('e'))  # Returns a list of all occurrence of the pattern
print(s.str.swapcase())  # Swaps the case lower/upper
print(s.str.islower())  # Checks whether all characters in each string in the Series/Index in lower case or not
print(s.str.isupper())
print(s.str.isnumeric()) #Checks whether all characters in each string in the Series/Index are numeric. Returns Boolean.