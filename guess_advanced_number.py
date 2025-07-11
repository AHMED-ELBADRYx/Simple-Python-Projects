# Guess a number from 1 to 10

import random
from time import sleep

class NumberGuesser:
    def __init__(self):
        self.min_range = 1
        self.max_range = 100
        self.max_attempts = 7
        self.score = 0
        self.high_score = 0

    def display_welcome(self):
        """Show welcome message and instructions"""
        print("🎲 Welcome to the Ultimate Number Guessing Game! 🎲")
        print("="*50)
        print(f"I'm thinking of a number between {self.min_range} and {self.max_range}.")
        print(f"Can you guess it in {self.max_attempts} attempts or less?")
        print("\n💡 Tip: After each guess, I'll tell you if you're too high or too low!")
        print("="*50)
        sleep(1)

    def get_difficulty(self):
        """Let player select difficulty level"""
        print("\nDifficulty Levels:")
        print("1. Easy (1-50, 10 attempts)")
        print("2. Medium (1-100, 7 attempts)")
        print("3. Hard (1-200, 5 attempts)")
        
        while True:
            try:
                choice = int(input("Select difficulty (1-3): "))
                if choice == 1:
                    self.min_range, self.max_range, self.max_attempts = 1, 50, 10
                elif choice == 2:
                    self.min_range, self.max_range, self.max_attempts = 1, 100, 7
                elif choice == 3:
                    self.min_range, self.max_range, self.max_attempts = 1, 200, 5
                else:
                    print("Please enter 1, 2, or 3")
                    continue
                break
            except ValueError:
                print("Please enter a valid number")

    def get_guess(self, attempt):
        """Get and validate player's guess"""
        while True:
            try:
                guess = int(input(f"\nAttempt {attempt}/{self.max_attempts}: Enter your guess: "))
                if self.min_range <= guess <= self.max_range:
                    return guess
                print(f"Please enter a number between {self.min_range} and {self.max_range}")
            except ValueError:
                print("Please enter a valid number")

    def play_round(self):
        """Play one round of the game"""
        secret_number = random.randint(self.min_range, self.max_range)
        attempts = 0
        
        print(f"\n🔍 I've picked a number between {self.min_range} and {self.max_range}...")
        sleep(1)
        
        while attempts < self.max_attempts:
            attempts += 1
            guess = self.get_guess(attempts)
            
            if guess == secret_number:
                self.score = self.max_attempts - attempts + 1
                if self.score > self.high_score:
                    self.high_score = self.score
                print(f"\n🎉 Congratulations! You guessed it in {attempts} attempt{'s' if attempts != 1 else ''}!")
                print(f"🏆 Score: {self.score} | High Score: {self.high_score}")
                return True
            elif guess < secret_number:
                print("⬆ Too low!")
            else:
                print("⬇ Too high!")
        
        print(f"\n💔 Game over! The number was {secret_number}")
        return False

    def play_game(self):
        """Main game loop"""
        self.display_welcome()
        self.get_difficulty()
        
        while True:
            self.play_round()
            
            if input("\nPlay again? (yes/no): ").lower() not in ['yes', 'y']:
                print(f"\nThanks for playing! Your final high score was {self.high_score}")
                print("👋 Goodbye!")
                break

if __name__ == "__main__":
    game = NumberGuesser()
    game.play_game()