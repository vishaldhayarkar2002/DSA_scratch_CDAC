class Employee:
    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def display(self):
        print(self.first_name, self.last_name)
        print("Monthly Salary:", self.salary)

    def increase_salary(self):
        self.salary = self.salary + (self.salary * 10 / 100)

    def yearly_salary(self):
        return self.salary * 12


print("Enter Employee 1:")
name1 = input("First name: ")
last1 = input("Last name: ")
salary1 = float(input("Monthly salary: "))

print("\nEnter Employee 2:")
name2 = input("First name: ")
last2 = input("Last name: ")
salary2 = float(input("Monthly salary: "))

e1 = Employee(name1, last1, salary1)
e2 = Employee(name2, last2, salary2)

print("\nYearly Salary:")
print(e1.first_name, ":", e1.yearly_salary())
print(e2.first_name, ":", e2.yearly_salary())

e1.increase_salary()
e2.increase_salary()

print("\nAfter 10% Increase:")
print(e1.first_name, ":", e1.yearly_salary())
print(e2.first_name, ":", e2.yearly_salary())