def greatNum():
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter a number: "))
    num3 = int(input("Enter a number: "))

    if(num1 > num2 and num1 > num3):
        print(f"This is the greatest number: {num1}")
    elif(num2 > num1 and num2 > num3):
        print(f"This is the greatest number: {num2}")
    else:
        print(f"This is the greatest number: {num3}")

greatNum()