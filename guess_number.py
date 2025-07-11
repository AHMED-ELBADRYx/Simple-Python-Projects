# Guess the number

import random

def play_game():
    """Play a single round of the guessing game"""
    secret_number = random.randint(1, 10)
    attempts = 0
    max_attempts = 5
    
    print("\n🔢 I've picked a number between 1 and 10. Can you guess it?")
    print(f"You have {max_attempts} attempts to guess correctly.")
    
    while attempts < max_attempts:
        try:
            guess = int(input(f"\nAttempt {attempts + 1}/{max_attempts}: Your guess (1-10): "))
            
            if guess < 1 or guess > 10:
                print("⚠ Please enter a number between 1 and 10!")
                continue
                
            attempts += 1
            
            if guess == secret_number:
                print(f"🎉 Congratulations! You guessed it in {attempts} attempt{'s' if attempts != 1 else ''}!")
                return True
            elif guess > secret_number:
                print("⬇ Too high! Try a lower number.")
            else:
                print("⬆ Too low! Try a higher number.")
                
        except ValueError:
            print("❌ Invalid input. Please enter a number between 1 and 10!")
    
    print(f"\n💔 Game over! The secret number was {secret_number}.")
    return False

def main():
    print("🌟 Welcome to the Number Guessing Game! 🌟")
    print("----------------------------------------")
    
    while True:
        play_game()
        
        if input("\nWould you like to play again? (yes/no): ").lower() not in ['yes', 'y']:
            print("\nThanks for playing! Goodbye 👋")
            break

if __name__ == "__main__":
    main()