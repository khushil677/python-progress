# Basic way to create a class
class Employee:
    language = "Py"
    salary = 12000000

harry = Employee()
harry.name = "Harry"
print(harry.name, harry.language, harry.salary)

khushil = Employee()
khushil.name = "Khushil"
print(khushil.name, khushil.salary)

# Here the name is an instance (object) attribute and language and salary are both class attributes as they belong directly to the class!