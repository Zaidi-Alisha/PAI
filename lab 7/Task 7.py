import numpy as np
array = np.random.rand(1000)
print(array)
average = np.mean(array)
variance = np.var(array)
deviation =np.std(array)

result = f"average:{average}, variance: {variance}, deviation: {deviation}"
filename = "results.txt"
with open (filename, 'w') as file:
    file.write(result)