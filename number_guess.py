# Python Project: Number Guessing Game
# Build a terminal game where the user guesses a randomly generated number.

# Import Required Module
# import random

# Generate Random Number
# number = random.randint(1, 100)
# inludes :
# Loop Until User Guesses Right 
# - Random number generation  
# - Loops  
# - Conditionals  
# - User input & conversion  
# - Game logic

import random

number = random.randint(1, 100)
attempts = 0

print(" Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

while True:
    try:
        guess = int(input("Guess a number (1-100): "))
        attempts += 1

        if guess < 1 or guess > 100:
            print(" Please guess within 1 to 100.")
            continue

        if guess < number:
            print(" Too low!")
        elif guess > number:
            print(" Too high!")
        else:
            print(f" Correct! You guessed it in {attempts} attempts!")
            break

    except ValueError:
        print(" Please enter a valid number.")