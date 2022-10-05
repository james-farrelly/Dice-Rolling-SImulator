import random

sides = int(input("How many sides would you like the dice to have?"))

while True:
    reroll = input("Roll the dice? (Yes/No)").upper()
    if reroll == "YES":
        number = random.randint(1, sides)
        print("You rolled a", number)
        continue
    else:
        break