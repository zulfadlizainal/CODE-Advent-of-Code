import pandas as pd
from collections import Counter

df = pd.read_csv('data.txt', header= None)

df.columns = ['Original']
df[['Policy','Key','Password']] = df['Original'].str.split(expand=True)
df[['Policy_Min','Policy_Max']] = df['Policy'].str.split('-',expand=True)
df[['Key_2','Dummy']] = df['Key'].str.split(':',expand=True)

df[['Policy_Min','Policy_Max']] = df[['Policy_Min','Policy_Max']].astype(int)

del df['Dummy']



