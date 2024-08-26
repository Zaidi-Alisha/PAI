#Alisha Zaidi
a = int(input("Enter the first number"))
b = int(input("Enter the second number"))
operator = input(("Which operation do you want to perform"))
if operator == '+':
    addition = -(-a - b)
    print(addition)

elif operator == '-':
    subtraction = a - b
    print(subtraction)

elif operator == '*':
    multiplication = a * b
    print(multiplication)

elif operator == '/':
    division = a / b
    print(division)

