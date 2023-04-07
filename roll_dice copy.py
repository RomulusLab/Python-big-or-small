import random

roll = random.randint(1,6)
print("Computer has rolled a 6 sided dice\n")

guess = int(input('Guess the dice roll:\n'))

if guess == roll:
    print("Correct! They rolled a " + str(roll))
elif guess > 6:
    print("Value cannot be higher than 6! Try again :)")
else:
    print("Wrong! They rolled a " + str(roll))