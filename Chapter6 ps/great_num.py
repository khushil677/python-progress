#prints the greatest number

num_one = int(input("Enter a num: "))
num_two = int(input("Enter a num: "))
num_three = int(input("Enter a num: "))
num_four = int(input("Enter a num: "))

if(num_one > num_two and num_three and num_four):
    print(num_one)

elif(num_two > num_three and num_four and num_one):
    print(num_two)

elif(num_three > num_two and num_one and num_four):
    print(num_three)

else:
    print(num_four)