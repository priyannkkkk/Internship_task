import numpy as np
import pandas as pd

# Defining file Path
f_gender = r"D:\Data Science\Task_2\gender_submission.csv"
f_train = r"D:\Data Science\Task_2\train.csv"
f_test = r"D:\Data Science\Task_2\test.csv"

# Load Csv file
df_gender = pd.read_csv(f_gender)
df_train = pd.read_csv(f_train)
df_test = pd.read_csv(f_test)

'''
print(df_test.head())
print(df_gender.head())
print(df_train.head())
'''

#print(df_gender.isnull().sum())
print(df_test.isnull().sum())

df_test['Age'] = df_test['Age'].fillna(df_test['Age'].median())

print(df_test.info())
