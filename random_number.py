# Random Number Guessing Game in Python

import random

counter = 6
ran_com = random.randint(1, 100)

while counter > 0:
    try:
        ran_user = int(input("Guess the number (1-100): "))
        
        if ran_user > ran_com:
            print("Too high!")
        elif ran_user < ran_com:
            print("Too low!")
        else:
            print("Congratulations! 🎉 You guessed the right number!")
            break  # Exit the loop if the guess is correct

        counter -= 1  # Decrease attempts after each wrong guess
        print(f"Attempts left: {counter}")  # Show remaining attempts

    except ValueError:
        print("Invalid input! Please enter a number between 1 and 100.")

if counter == 0:
    print(f"Game Over! The correct number was {ran_com}.")