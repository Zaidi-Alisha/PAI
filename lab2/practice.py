'''Practise task1'''
def print_greeting():
    print("Hello")


print_greeting()


'''Practise task2'''
def calculate_area(length, width):
    area = length * width
    print(area)


calculate_area(2, 3)


'''Practise task3'''
def find_maximum(*numbers):
    maximum = numbers[0]
    for num in numbers[1:]:
        if num > maximum:
            maximum = num
    print(maximum)


find_maximum(3,4,5,6,2)
find_maximum(54,23,23, -54)


'''Lambda'''

multiplication = lambda x, y, z : x * y * z
print(multiplication(5, 6, 2))

'''Example'''
name = input("What is your name?")
name_title = name.title()
print("Hello!", name_title, "I hope you are fine, let me know how I can help you!")
choice = input("")
if choice == 'Yes' or 'yes':
    enter = input("Share your problem with us")
    print("Thanks for your feedback,we will resolve your problem")

elif choice == 'No' or 'no':
    string = "Okay! Good to see you, stay connected"
    string.center(20)