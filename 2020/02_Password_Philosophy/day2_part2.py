data = open("data.txt", "r")

result = 0

for index in data.readlines():
    
    index = index.split()
    policy_min, policy_max = map(int,index[0].split('-'))
    key = index[1][0]
    
    if (index[2][policy_min-1] == key) ^ (index[2][policy_max-1] == key):
        result = result + 1
    
print(result)