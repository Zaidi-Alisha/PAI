class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name

    def display_info(self):
        print("Student ID: ", self.student_id)
        print("Student Name: ", self.name)

class Marks(Student):
    def __init__(self, student_id, name, marks_algo, marks_dataScience, marks_calculus):
        super().__init__(student_id, name)
        self.marks_algo = marks_algo
        self.marks_dataScience = marks_dataScience
        self.marks_calculus = marks_calculus

    def display_marks(self):
        print("Algorithm Marks: ", self.marks_algo)
        print("Data Science Marks: ", self.marks_dataScience)
        print("Calculus Marks: ", self.marks_calculus)

class Result(Marks):
    def __init__(self, student_id, name, marks_algo, marks_dataScience, marks_calculus):
        super().__init__(student_id, name, marks_algo, marks_dataScience, marks_calculus)

    def calculate_result(self):
        total_marks = self.marks_algo + self.marks_dataScience + self.marks_calculus
        average_marks = total_marks / 3
        print("Total Marks: ", total_marks)
        print("Average Marks: ", average_marks)

student_result = Result(4567, "Alisha", 98, 76, 89)
student_result.display_info()   
student_result.display_marks()         
student_result.calculate_result()       

