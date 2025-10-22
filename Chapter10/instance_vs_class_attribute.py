class Employee:
    language = "Py"
    salary = 12000000

harry = Employee()
harry.language = "js" #This will override because it is an instance attribute
print( harry.language, harry.salary)