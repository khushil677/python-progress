class Calculator:
    def __init__(self, n):
        self.n = n

    def square(self):
        print(f"The square is {self.n*self.n}")

    def Cube(self):
        print(f"The cube is {self.n*self.n*self.n}")

    def SquareRoot(self):
        print(f"The square root is {self.n**1/2}")

a = Calculator(21)
a.square()
a.Cube()
a.SquareRoot()