list = input("Enter a list of numbers separated by spaces: ")
list = list(map(int, list.split()))

a = int(input("Enter a number: "))

newList = [i for i in list if i >= a]

print(newList)
