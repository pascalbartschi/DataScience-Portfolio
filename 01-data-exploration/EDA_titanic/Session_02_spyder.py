# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 21:02:06 2022

@author: pascal
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df_test = pd.read_csv('data/test.csv', sep =',')
df_train = pd.read_csv('data/train.csv', sep=',')

df_train_cleaned = df_train.dropna(subset=['Age'])
df_test_cleaned = df_test.dropna(subset=['Age'])
df_train_cleaned['Age'].values

# print('test:', df_test['Age'])
# print('cleaned',df_test_cleaned['Age'])

arr = df_train_cleaned['Age'].to_numpy(dtype='int')

# help(pd.concat)

# this creates a list of dataframes
df_list = [df_train, df_test]
print(type(df_list))

# combine the two dataframes
df_combined = pd.concat(df_list, sort=True)
df_combined.describe()

print(df_combined.head())

## masking

df_combined[df_combined['Name'] == 'Kelly, Mr. James'] # look in row for Kelly Mrs. James 
# creates boolean area of condition which has to be satisfied, work this out at home
print(df_combined[df_combined['Name'] == 'Kelly, Mr. James'].head())

help(plt.hist)


df_combined['Age'].hist(density = True)
df_combined['Age'].plot.kde()


print(df_combined['Pclass'].value_counts())

sct = plt.scatter(df_combined['Age'], df_combined['Fare'], c = df_combined['Survived'])
cbar = plt.colorbar(sct)
cbar.set_label('SUrvivors')

#%%

sct2 = plt.scatter(df_combined['Survived'], df_combined['Fare'], s= 1)

df_combined['Survived'].hist()
df_combined['Fare'].hist()
df_combined['Pclass'].hist()

#%%

sct3 = plt.scatter(df_combined['Survived'], df_combined['Fare'], c = df_combined['Pclass'], s= 5)
cbar3 = plt.colorbar(sct3)
cbar3.set_label('Pclass')

#%%

# you need to compute survivors per class

bar = plt.bar(df_combined['Pclass'], df_combined['Survived'])

#%%

for row in df_combined['Age']:
    print(row)



