import numpy as np
import pandas as pd

# Define file path
f_total = r"D:\Data Science\task oe\Total_Population.csv"
f_male = r"D:\Data Science\task oe\Male_Population.csv"
f_female = r"D:\Data Science\task oe\Female_Population.csv"

# Load csv files as dataframe
# using skiprows=4 to skip meta data rows
df_total = pd.read_csv(f_total,skiprows=4)
df_male = pd.read_csv(f_male,skiprows=4)
df_female = pd.read_csv(f_female,skiprows=4)

# Displaying first five rows
print(df_total.head())
print(df_male.head())
print(df_female.head())