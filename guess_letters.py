# Guess the letters of the word

import random
from string import ascii_lowercase

class WordGuesser:
    def __init__(self):
        self.words = ["python", "programming", "developer", "algorithm", "function"]
        self.secret_word = ""
        self.display = []
        self.guessed_letters = set()
        self.attempts = 0
        self.max_attempts = 7

    def select_word(self):
        """Select a random word and initialize game state"""
        self.secret_word = random.choice(self.words).lower()
        self.display = ["_" for _ in self.secret_word]
        self.guessed_letters = set()
        self.attempts = 0

    def display_status(self):
        """Show current game status"""
        print(f"\nWord: {' '.join(self.display)}")
        print(f"Guessed letters: {' '.join(sorted(self.guessed_letters))}")
        print(f"Attempts remaining: {self.max_attempts - self.attempts}")
        print(f"Progress: {self.get_progress()}")

    def get_progress(self):
        """Calculate completion percentage"""
        revealed = sum(1 for char in self.display if char != "_")
        return f"{int((revealed/len(self.secret_word))*100)}% complete"

    def process_guess(self, letter):
        """Process a letter guess"""
        self.guessed_letters.add(letter)
        
        if letter in self.secret_word:
            for i, char in enumerate(self.secret_word):
                if char == letter:
                    self.display[i] = letter
            return True
        else:
            self.attempts += 1
            return False

    def get_valid_letter(self):
        """Get and validate user input"""
        while True:
            letter = input("\nEnter a letter: ").strip().lower()
            if len(letter) != 1:
                print("Please enter exactly one character.")
            elif letter not in ascii_lowercase:
                print("Please enter an English letter (a-z).")
            elif letter in self.guessed_letters:
                print("You've already guessed that letter.")
            else:
                return letter

    def play(self):
        """Main game loop"""
        print("🌟 Welcome to the Letter Guessing Game! 🌟")
        print("----------------------------------------")
        print(f"Guess the letters to reveal the hidden word (Max attempts: {self.max_attempts})")
        
        self.select_word()
        
        while "_" in self.display and self.attempts < self.max_attempts:
            self.display_status()
            
            letter = self.get_valid_letter()
            correct = self.process_guess(letter)
            
            if correct:
                print("\n✅ Correct! The letter is in the word.")
            else:
                print(f"\n❌ Incorrect! That letter is not in the word. ({self.max_attempts - self.attempts} attempts remaining)")

        self.display_status()
        
        if "_" not in self.display:
            print(f"\n🎉 Congratulations! You guessed the word '{self.secret_word}' in {len(self.guessed_letters)} guesses!")
        else:
            print(f"\n💔 Game over! The word was: {self.secret_word}")

        if input("\nPlay again? (y/n): ").lower() == "y":
            self.play()
        else:
            print("\nThanks for playing! Goodbye 👋")

if __name__ == "__main__":
    game = WordGuesser()
    game.play()