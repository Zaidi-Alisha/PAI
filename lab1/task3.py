#Alisha Zaidi
user = list(input("Enter the integers in the list"))
print(user)
count = 0
for i in user:
    check = int(i) % 2
    if check == 0:
        count += 1
print(count)