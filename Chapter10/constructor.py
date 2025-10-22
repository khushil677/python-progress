class Employee:

    def __init__(self, name, salary, language): #Dunder Method, dunder methods are automatically called
        self.name = name
        self.salary = salary
        self.language = language
        print("I am creating an object")


    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod
    def greet():
        print("good")

harry = Employee("Khushil", 1323343424, "python")
print(harry.name, harry.salary, harry.language)



