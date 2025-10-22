class Employee:
    company = "Walmart"
    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary}")


# class Programmer:
    # def show(self):
    #     print(f"The name is {self.name} and the salary is {self.salary}")

    # def showLanguage(self):
    #     print(f"The name is {self.name} and he is good in {self.language} language")

class Programmer(Employee):
    def showLanguage(self):
        print(f"The name is {self.name} and he is good in {self.language} language")


a = Employee()

print(a.company)