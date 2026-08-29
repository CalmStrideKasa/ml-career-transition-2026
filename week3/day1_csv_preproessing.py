import pandas as pd

df = pd.read_csv('data/housing.csv')

df['total_bedrooms'] = df['total_bedrooms'].fillna(df['total_bedrooms'].mean())
df = pd.get_dummies(df, columns=['ocean_proximity'])

print(df.columns)
print(df.isnull().sum())
print(df.head())