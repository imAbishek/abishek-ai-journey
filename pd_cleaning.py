import pandas as pd

df = pd.read_csv('properties.csv')

df.info()

print("\n--- Null counts before cleaning ---")
print(df.isnull().sum())
df['price_lakhs'] = df['price_lakhs'].fillna(df['price_lakhs'].median())
df['area_sqft'] = df['area_sqft'].fillna(df['area_sqft'].median())
df = df.dropna(subset=['city'])
print("\n--- Null counts after cleaning ---")
print(df.isnull().sum())

city = df['city'].value_counts()
print("\n--- City name's before fixing ---")
print(city)

df['city'] = df['city'].str.strip().str.title()
city = df['city'].value_counts()
print("\n--- City name's after fixing ---")
print(city)

apartments = df[df['type'] == 'apartment']
print("\n--- Type Apartments only data ---")
print(apartments)

summary = df.groupby('city')['price_lakhs'].mean()
print("\n--- Groupby price based on the city ---")
print(summary)

print("\n--- Based on City name's get specific columns ---")
print(df.loc[df['city'] == 'Coimbatore',['city' ,'price_lakhs']])