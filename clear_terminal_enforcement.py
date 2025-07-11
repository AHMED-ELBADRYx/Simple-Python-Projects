# Enforcement on clear terminal

import os
import random

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

secret_number = random.randint(1, 10)

while True:
    try:
        user_guess = int(input("Enter a number between 1 and 10: ").strip())

        if 1 <= user_guess <= 10:
            if user_guess == secret_number:
                print("\n🎉 CONGRATULATIONS! You guessed it!")
                break
            else:
                print("❌ Incorrect, try again.")
        else:
            print("⚠ Please enter a number between 1 and 10.")

        input("\nPress Enter to continue...")
        clear_terminal()

    except ValueError:
        print("❌ Invalid input. Please enter a valid number.")
        input("\nPress Enter to continue...")
        clear_terminal()