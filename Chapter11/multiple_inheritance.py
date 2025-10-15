class Employee:
    company = "Walmart"
    name = "Khushil"
    salary = 13224
    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary}")

class Coder:
    language = "Python"
    def printLanguages(self):
        print(f"Out of all the languages, here is your language {self.language}")

class Programmer(Employee, Coder):
    def showLanguage(self):
        print(f"The name is {self.name} and he is good in {self.language} language")


a = Employee()
b = Programmer()

b.show()
b.printLanguages()
b.showLanguage()