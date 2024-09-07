try:
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))

    result = a / b

    print("Result:", result)

except ValueError:
    print("Please enter integers to perform division")
    
except ZeroDivisionError:
    print("Please enter a non-zero number because division by zero results in infinity")

