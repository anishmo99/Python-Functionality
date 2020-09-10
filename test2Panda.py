# Import pandas library
import pandas as pd
import numpy as np

# Read the online file by the URL provides above, and assign it to variable "df"
other_path = "auto.csv"
df = pd.read_csv(other_path, header=None)
print(df)
headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]
df.columns=headers
df=df.dropna(subset=['price'],axis=0)
df.replace('?', np.nan,inplace=True)
print(df.head(10))