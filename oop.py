#oop
# object --> laptop
# name--> props
# classes
from Numbers import result


class Person:
    # constructor
    def __init__(self, name, dob, race,weight,height):
        self.name = name
        self.dob = dob
        self.race = race
        self.weight = weight
        self.height = height
    def display(self):
        print(f"Name is {self.name} and DOB is {self.dob}")

    def get_bmi(self):
        result = self.weight/self.height**2
        return round(result,2)

# blueprint for creating objects
p1 = Person("Chris Thyme", "26-10-2006","Black",64.49,1.54)
p2: Person= Person("Jane Doe", "31-09-2001","White",70.99,1.74)

p1.display()
p2.display()
# print(p1.get_bmi())
print(f"{p1.name}'s bmi is {p1.get_bmi()}") #ctrl+D to duplicate
print(f"{p2.name}'s bmi is {p2.get_bmi()}")

