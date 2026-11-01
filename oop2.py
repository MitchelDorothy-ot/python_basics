#oop2
class Circle:
    def __init__(self, r): #setup
        self.radius = r

    def area(self):
        return 22/7 * self.radius**2

    def perimeter(self):
        return 22/7 * self.radius* 2

    def print_details(self):
        print("Radius is",self.radius)
        print("Area is",self.area)
        print("Perimeter is",self.perimeter)

c1 = Circle(10)
c2 = Circle(28)
c3 = Circle(40)

print(c1.area())
c1.print_details()

#oop2
class Circle:
    def __init__(self, r): #setup
        self.radius = r

    def area(self):
        return 22/7 * self.radius**2

    def perimeter(self):
        return 22/7 * self.radius* 2

    def print_details(self):
        print("Radius is",self.radius)
        print("Area is",self.area())
        print("Perimeter is",self.perimeter())

c1 = Circle(10)
c2 = Circle(28)
c3 = Circle(40)

print(c1.area())
c1.print_details()

# branch -- copy --master main
# feature --

# we are learning inheritance python

