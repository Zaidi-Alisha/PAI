class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_bonus(self):
        pass

class Manager(Employee):
    def calculate_bonus(self):
        return self.salary * 0.20

    def hire(self):
        print(" ", self.name, "hires a new employee")

class Developer(Employee):
    def calculate_bonus(self):
        return self.salary * 0.10

    def write_code(self):
        print(" ", self.name, "writes code")

class SeniorManager(Manager):
    def calculate_bonus(self):
        return self.salary * 0.30


manager = Manager("Amna", 56786)
developer = Developer("Sam", 24567)
senior_manager = SeniorManager("Farwa", 67894)

print(f"Bonus of manager {manager.name} is {manager.calculate_bonus()}")
manager.hire()

print(f"Bonus of developer {developer.name} is {developer.calculate_bonus()}")
developer.write_code()

print(f"Bonus of senior manager {senior_manager.name} is {senior_manager.calculate_bonus()}")
