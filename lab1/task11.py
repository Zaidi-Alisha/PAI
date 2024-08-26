subject1 = int(input("Enter marks for subject 1: "))
subject2 = int(input("Enter marks for subject 2: "))
subject3 = int(input("Enter marks for subject 3: "))

dictionary = {"subject 1": subject1, "subject 2": subject2, "subject 3": subject3}

total = 0
subjects = 0

for mark in dictionary.values():
    total += mark
    subjects += 1

average = total / subjects

percentage = (total/ (subjects * 100)) * 100

print(f"Average marks: {average:.2f}")
print(f"Percentage: {percentage:.2f}%")
