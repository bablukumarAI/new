class Rectangle:
    def __init__(self):
        self.length = int(input("Enter length of Rectangle :"))
        self.breadth =int(input("Enter breadth of Rectangle :"))

    def Area(self):
        area1 = self.length * self.breadth
        return area1

r1 = Rectangle()
print("Area of rectange :", r1.Area())