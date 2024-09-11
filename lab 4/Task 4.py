class Employee:
    def __init__(self, name, salary, tax_percentage=2):
        self.name = name
        self.salary = salary
        self.tax_percentage = tax_percentage

    def get_data(self):
        self.name = input("What is the employee name: ")
        self.salary = float(input("What is monthly salary: "))
        self.tax_percentage = float(input("Enter tax percentage: "))

    def Salary_after_tax(self):
        tax_amount = self.salary * (self.tax_percentage / 100)
        return self.salary - tax_amount

    def update_tax_percentage(self, new_tax_percentage):
        self.tax_percentage = new_tax_percentage

employee = Employee("Alisha", 45678)
print(employee.Salary_after_tax())  
employee.update_tax_percentage(3)   
print(employee.Salary_after_tax()) 

