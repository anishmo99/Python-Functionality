import pandas as pd

print(pd.get_option("display.max_rows"))  # displays default number of rows value
# same for columns
pd.set_option("display.max_rows", 80)
print(pd.get_option("display.max_rows"))
# same for columns
pd.reset_option("display.max_rows")
print(pd.get_option("display.max_rows"))
pi = 3.14159265
pd.set_option("display.precision", 5)
# now just simply print the dataframe.
print("{0:.5f}".format(pi))
