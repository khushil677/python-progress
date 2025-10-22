# Guess the right number!
import random

random_num = random.randint(1, 2000)

guess = 0


while True:
    player_one = int(input("Guess a number: "))
    guess += 1

    if (player_one == random_num):
        print(f"The number was {random_num} and you guessed it correctly!")
        break

    elif (player_one > random_num):
        print("Try guessing a lower number")

    else:
        print("Try guessing a higher number!")

print(f"You took {guess} tries to get it right!")