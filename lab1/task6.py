a = float(input("Enter your marks in physics: "))
b = float(input("Enter your marks in chemistry: "))
c = float(input("Enter your marks in maths: "))

dictionary = {"Physics": a, "Chemistry": b, "Maths": c}
highest = 0
average = 0
for i in dictionary:
    if float(dictionary[i]) > highest:
        highest = float(dictionary[i])
    average += float(dictionary[i])

print("Highest marks are:", highest)
print("Average is: ", average/3)