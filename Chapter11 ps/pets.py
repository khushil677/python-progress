class Animals: 
    pass

class Pets(Animals):
    pass
    
class Dog(Pets):
    def bark():
        print("This is a dog! Bow Bow!")


d = Dog
d.bark()