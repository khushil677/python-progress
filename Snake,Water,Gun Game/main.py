import random
# 1 is for rock
# -1 is for paper
# # 0 for Scissors

computer = random.choice([-1, 0, 1])
youStr = input("Enter your choice (Rock, Paper or Scissors): ").lower()
youDict = {"rock": 1, "paper": -1, "scissors": 0}
reverseDict = {1 : "Rock", -1 : "Paper", 0 : "Scissors"}

you = youDict[youStr]

print(f"You chose {reverseDict[you]} \nComputer chose {reverseDict[computer]}")

if(computer == you):
    print("It is a draw!")


else:
    if(computer == 1 and you == -1):
        print("You Won!")

    elif(computer == -1 and you == 1):
        print("Computer won!")

    if(computer == 0 and you == 1):
        print("You won!")

    elif(computer == 1 and you == 0):
        print("Computer Won!")

    if(computer == -1 and you == 0):
        print("You won!")

    elif(computer == 0 and you == -1):
        print("Computer Won!")

