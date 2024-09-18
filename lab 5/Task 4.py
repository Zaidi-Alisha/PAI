class Student:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def display(self):
        print("ID: ", self.id)
        print("Name: ", self.name)


class Marks(Student):
    def __init__(self, id, name, marks_algo, marks_dataScience, marks_calculus):
        super().__init__(id, name)
        self.marks_algo = marks_algo
        self.marks_dataScience = marks_dataScience
        self.marks_calculus = marks_calculus

    def display_marks(self):
        print("Algorithm Marks: ", self.marks_algo)
        print("Data Science Marks: ", self.marks_dataScience)
        print("Calculus Marks: ", self.marks_calculus)


class Result(Marks):
    def __init__(self, id, name, marks_algo, marks_dataScience, marks_calculus):
        super().__init__(id, name, marks_algo, marks_dataScience, marks_calculus)

    def calculate(self):
        total = self.marks_algo + self.marks_dataScience + self.marks_calculus
        average = total / 3
        print("Total Marks: ", total)
        print("Average Marks: ", average)

student = Result(345, "Alisha Zaidi", 87, 93, 75)
student.display()
student.display_marks()
student.calculate()
