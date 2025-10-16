class TwoDVector:
    def __init__(self, i, j):
        self.i = i
        self.j = j

    def show(self):
        print(f"The vector is {self.i}i + {self.j}j ")
        
class ThreeDVector(TwoDVector):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.k = k
        
    def show(self):
        print(f"The vector is {self.i}i + {self.j}j + {self.j}k ")

o = TwoDVector(1, 2)
b = ThreeDVector(3, 4, 5)

o.show()
b.show()