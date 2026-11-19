
import random

pos = 0

while pos < 100:
    input("Press Enter to roll dice")

    dice = random.randint(1, 6)
    print("Dice:", dice)

    pos = pos + dice

    if pos > 100:
        pos = pos - dice

    if pos == 10:
        pos = 25
        print("you got a ladder")

    elif pos == 30:
        pos = 5
        print("Snake bites,,,,")

    elif pos == 50:
        pos = 75
        print("you got a ladder")

    elif pos == 90:
        pos = 40
        print("Snake bites,,,,")

    print("Current Position:", pos)

print("Congratulations! You Won!")