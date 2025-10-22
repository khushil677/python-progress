import random

def game():
    print("You are playing the game...")
    score = random.randint(1, 100)

    try:
        with open("hi-score.txt") as f:
            hi_score = f.read()
            hi_score = int(hi_score) if hi_score.strip() != "" else 0
    except FileNotFoundError:
        hi_score = 0

    print(f"Your score is: {score}")
    if score > hi_score:
        print("New high score!")
        with open("hi-score.txt", "w") as f:
            f.write(str(score))

    return score

game()
