class Employee:
    language = "Py"
    salary = 12000000

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    def greet(self):
        print("good")

harry = Employee()
harry.language = "js" #This will override because it is an instance attribute

harry.getInfo()
harry.greet()
