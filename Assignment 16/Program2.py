class circle:
    PI = 3.14
    def __init__(self_):
        Radius = 0.0
        Area = 0.0
        Circumference = 0.0

    def Accept(self):
        print("enter radius of circle")
        self.Radius = float(input())

    def CalculateArea(self):
        self.Area = 0.0
        self.Area = circle.PI * self.Radius * self.Radius

    def Circumference(self):
        self.Circumference = 2 * circle.PI * self.Radius

    def Display(self):
        print("Radius of circle is:",self.Radius)
        print("Area of circle :",self.Area)
        print("Circumference is :",self.Circumference)

cobj = circle()
cobj.Accept()
cobj.CalculateArea()
cobj.Circumference()
cobj.Display()