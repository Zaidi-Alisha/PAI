a = input("Enter a list of numbers separated by spaces: ")

list = list(map(int, a.split()))

max = max(list)

print(max)
