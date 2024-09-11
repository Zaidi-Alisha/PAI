class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def print_biodata(self):
        print(f"Name: {self.name}, Age: {self.age}")

student = Student("Alisha", 19)
student.print_biodata() 

