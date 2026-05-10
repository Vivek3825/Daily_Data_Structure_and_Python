class Circle:
    pie = 22/7
    def __init__(self, radius):
        self. radius = radius

    def Area(self):
        print(f"Area of circle is: {Circle.pie * self.radius ** 2}")

    def Perimeter(self):
        print(f"Area of circle is: {2 * Circle.pie * self.radius}")

circle1 = Circle(21)

circle1.Area()
circle1.Perimeter()