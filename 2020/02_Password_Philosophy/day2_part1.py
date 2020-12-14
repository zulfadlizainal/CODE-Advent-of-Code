data = open("data.txt", "r")

result = 0

for index in data.readlines():
    
    index = index.split()
    policy_min, policy_max = map(int,index[0].split('-'))
    key = index[1][0]
    
    if index[2].count(key) >= policy_min and index[2].count(key) <= policy_max:
        result = result + 1
    
print(result)