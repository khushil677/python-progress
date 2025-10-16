try:
    a = int(input("Hey, ENter a number: "))
    print(a)

except Exception as e:
    print(e)

#Without the except, if i entered a string instead of an int, the program would give me an error
#but with except, the program prints something like this,
# Hey, ENter a number: khuh
#invalid literal for int() with base 10: 'khuh'
#this makes the program work, but tells you where you went wrong
