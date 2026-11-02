# Inheritance
class Employee:
    def __init__(self, name, email, department, salary):
        self.tenure = None
        self.name = name
        self.email = email
        self.department = department
        self.salary = salary
        print(self.name, self.department, self.salary)


class PermanentEmployee(Employee):  # inheriting
    def __init__(self, name, email, department, salary, cover, increment):
        super().__init__(name, email, department, salary)
        self.cover = cover
        self.increment = increment

class ContractEmployee(Employee):
    def __init__(self, name, email, department, salary, tenure):
        super().__init__(name, email, department, salary)
        self.tenure = tenure

    def show_details(self):
        print(f"Name{self.name}")
        print(f"Email{self.email}")
        print(f"Contract Length{self.tenure}")

p1 = PermanentEmployee("John Mark", "jm@gmail.com", "HR", "100_000", "CIC", "10_000")
c2 = ContractEmployee("Chris Kaiga", "ck@gmail.com", "IT", "70_000", "3")

# p1.show_details()
c2.show_details()

# oop in python
# classes in python
