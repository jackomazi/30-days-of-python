import pandas as pd
import numpy as np

df = pd.read_csv('.\day_25\hacker_news.csv')
print(df.head())
print(df.tail())

titles = df['title']
print(titles)

print(df.shape)

# Filter the titles which contain python
filtered_df = df[df['title'].str.contains('python', case=False, na=False)]

print(filtered_df)
