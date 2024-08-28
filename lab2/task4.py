def employee(name, salary=10200):
    tax = 0.02
    new_salary = salary * (1 - tax)

    print("Employee Name: ", name)
    print("Salary after 2% tax:",  new_salary)


# Example usage
employee("Alisha", 34567)
employee("Sara")

