class Programmer:
    def __init__(self, name, country, salary):
        self.name = name
        self.country = country
        self.salary = salary

    @staticmethod
    def greet(self):
        print("Hello")


khushil = Programmer("Khushil", "Kenya", 1200000)

print(khushil.name, khushil.country, khushil.salary)
Programmer.greet()