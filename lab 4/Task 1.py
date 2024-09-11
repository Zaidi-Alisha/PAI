list1 = ["He", "th", "i", "sal"]
list2 = ["llo", "is", "s", "man"]

result = [i + j for i, j in zip(list1, list2)]
print(result) 

print([i + j for i, j in zip(list1, list2)]) 
