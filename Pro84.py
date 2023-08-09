# python program creates a simple text-based 
# game called "Guess the Number."

import random

def guess_the_number():
    target_number = random.randint(1, 100)
    attemps = 0
    while True:
        guess = int(input("Guess the number between 1 to 100: " ))
        attemps += 1
        if guess < target_number:
            print("Too low! Try again")
        elif guess > target_number:
            print("Too High! Try again")
        else: 
            print("Congratulations! You Guessed the number in "+ attemps + "attempts ")
            break

print("Welcome to guess number!")
guess_the_number()