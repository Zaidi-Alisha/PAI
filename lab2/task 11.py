students = {"Alisha": [87, 78, 94], "Maria": [68, 92, 60], "Saba": [87, 86, 72]}

def add_grade(name, grade):
    if name in students:
        students[name].append(grade)
        print("Added grade ", grade, "for", name)
    else:
        print("Student " ,name, "does not exist.")

def calculate_average(name):
    if name in students:
        grades = students[name]
        if grades:
            average = sum(grades) / len(grades)
            print("Average grade for ", name, "is", average)
        else:
            print("No grades available for ", name)
    else:
        print("Student ", name, "does not exist.")

def add_student(name):
    if name not in students:
        students[name] = []
        print("Added student ", name)
    else:
        print("Student", name, "already exists.")

def remove_student(name):
    if name in students:
        del students[name]
        print("Removed student", name)
    else:
        print("Student", name, "does not exist.")

def main():
    add_student("Ali")
    add_grade("Ali", 73)
    add_grade("Saba", 62)
    calculate_average("Alisha")
    remove_student("Maria")
    calculate_average("Maria")

if __name__ == "__main__":
    main()
