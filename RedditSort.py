import pandas as pd

# assign dataset
data = pd.read_csv(r"C:\Users\TheD4\Desktop\r_relationships\2009-10_relationships.csv")                                       

# sort data frame
data.sort_values(["Score"], axis=0, ascending=[False], inplace=True)