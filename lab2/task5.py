def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result


enter = int(input("Enter a number to calculate its factorial: "))
print(f"The factorial of", enter, " is:", factorial(enter))

