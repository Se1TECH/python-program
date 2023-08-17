# python program to hangman
import random

def hangman():
    wordList = ["apple","banana","orange","grape","pineapple","kiwi","watermalon"]
    word = random.choice(wordList).lower()
    guessed_letters = []
    attempts = 6

    print("Welcome to hangman!")
    print("_ " * len(word))
    
    while True:
        guess = input("Enter a letter: ").lower()

        if guess.isalpha() and len(guess) == 1:
            if guess in guessed_letters:
                print("You already guessed that letter. Try again.")
                continue

            guessed_letters.append(guess)

            if guess in word:
                print("Correct guess.")
            else:
                attempts -= 1
                print("Wrong Guess!")
                print(f"Attempts left: {attempts}")

            masked_word = ""
            for letter in word:
                if letter in guessed_letters:
                    masked_word += letter + " "
                else:
                    masked_word += "_ " 
            
            print(masked_word.strip())
            if "_" not in masked_word:
                print("Congratulations! You guessed the word correctly.")
                break
            
            if attempts == 0:
                print("Game Over! You ran out of attempts. ")
                print(f"Tha word was: {word}")
                break
            
        else:
            print("Invalid Input. Please enter a single letter.")

#start the game
hangman()
