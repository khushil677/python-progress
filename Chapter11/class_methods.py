class Employee:
    a = 1

    @classmethod #This will show the value of the class and not the overriden value
    def show(cls):
        print(f"The class attribute value of a is {cls.a}")

e = Employee()
e.a = 45 # Trying to override the value of a, if the class method was not there, e.show would have printed 45!

e.show()