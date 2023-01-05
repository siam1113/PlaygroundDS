import pandas as pd

# Read the text file
df = pd.read_csv(
    r"C:\\Users\\HP\\Downloads\\unsed pv from all the pods.txt", sep=" ", header=None)

# Reading the first column from the dataframe
print(df[0])
