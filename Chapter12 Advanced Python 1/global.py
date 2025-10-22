a = 89 #Global variable

def fun():
    global a #This would basically change the global variable
    a = 3
    print(a)


fun()
print(a)

#3
#3