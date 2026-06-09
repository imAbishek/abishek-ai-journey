import pandas as pd

# prices = pd.Series([45.0, 30.0, 120.0, 55.0])
# prices = pd.Series([45.0, 30.0, 120.0, 55.0], index=['prop_1', 'prop_2', 'prop_3', 'prop_4'])
# print(prices)
# print(prices['prop_1'])  # access by label
#
# df = pd.DataFrame({
#     'city': ['Chennai', 'Coimbatore', 'Bangalore'],
#     'price_lakhs': [45.0, 30.0, 120.0],
#     'area_sqft': [850, 600, 2500]
# })
#
# print(df['price_lakhs'])
df = pd.read_csv('properties.csv')
# print(df)
# print(df.describe())
# print(df.value_counts())
# print(df['city'].value_counts())
# print(df['type'].value_counts())
df = df.dropna(subset=['city'])
# print(df.dropna(subset=['city']))
df['price_lakhs'] = df['price_lakhs'].fillna(df['price_lakhs'].median())
# print(df['price_lakhs'])
df['city'] = df['city'].str.strip().str.title()
# print(df['city'])
# print(len(df))

apartments = df[df['type'] == 'apartment']
# print(apartments)

summary = df.groupby('city')['price_lakhs'].mean()
# print(summary)
print(df.loc[df['city'] == 'Coimbatore',['city' ,'price_lakhs']])