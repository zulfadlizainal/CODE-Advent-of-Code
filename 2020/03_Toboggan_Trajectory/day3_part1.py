import pandas as pd

df = pd.read_csv('data.txt', header = None)
df = df[0].apply(lambda x: pd.Series(list(x)))

x = 0
y = 0
trees = 0
route = []

for index in range(len(df)-1):
    if x < len(df.columns)-1:
        x = x+3
        y = y+1
        route.append(df[x][y])
        if route[index] == '#':
            trees = trees+1

print(trees)



        