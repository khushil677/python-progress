a = int(input("Enter your age: "))

#if statement 1
if(a%2 == 0):
    print("a is even")

# If statement 2
if(a>18):
    print("You are above the age of consent!")
    print("Good for you!")

elif(a==18):
    print("You are 18")

else:
    print("You are below the age of consent")