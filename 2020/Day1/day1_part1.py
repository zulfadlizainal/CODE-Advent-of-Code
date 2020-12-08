import pandas as pd

df = pd.read_csv('data.txt', header = None)
df_list = df[0].tolist()

def index_num(data,totalsum):
    for i in range(len(data)):
        for j in range(i+1,len(data)):
            if data[i]+data[j] == totalsum: return(i,j)

index_position = index_num(df_list, 2020)
index_position = list(index_position)

comp_A = df_list[index_position[0]]
comp_B = df_list[index_position[1]]

result = comp_A*comp_B
