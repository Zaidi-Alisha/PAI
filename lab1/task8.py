for i in range(1, 51):
    #number is a multiple of both 3 and 5
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")

    #number is a multiple of 3
    elif i % 3 == 0:
        print("Fizz")

    #number is a multiple of 5
    elif i % 5 == 0:
        print("Buzz")

    #if it's not a multiple of 3 or 5
    else:
        print(i)
