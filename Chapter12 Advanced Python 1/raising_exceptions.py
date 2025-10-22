a = int(input("Enter a number: "))
b = int(input("Enter a number: "))

if(b == 0):
    raise ZeroDivisionError("Hey, our program does not allow to divide by Zero")
else:
    print(f"The division a/b is {a/b}")

#This gives us our custom error, such as
#raise ZeroDivisionError("Hey, our program does not allow to divide by Zero")