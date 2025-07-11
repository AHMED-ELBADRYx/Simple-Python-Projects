# Hangman

import random
import string
from enum import Enum

class Difficulty(Enum):
    EASY = 1
    MEDIUM = 2
    HARD = 3

def load_words(difficulty):
    """Load words based on difficulty level"""
    words = {
        Difficulty.EASY: ["apple", "house", "water", "happy", "music"],
        Difficulty.MEDIUM: ["elephant", "guitar", "mountain", "rainbow", "keyboard"],
        Difficulty.HARD: ["extravaganza", "quintessential", "xylophone", "jazzercise", "subconscious"]
    }
    return random.choice(words[difficulty]).lower()

def display_hangman(tries):
    """Display hangman status based on remaining tries"""
    stages = [
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |      
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|
           |      |
           |     
           -
        """,
        """
           --------
           |      |
           |      O
           |      |
           |      |
           |     
           -
        """,
        """
           --------
           |      |
           |      O
           |    
           |      
           |     
           -
        """,
        """
           --------
           |      |
           |      
           |    
           |      
           |     
           -
        """
    ]
    return stages[tries]

def display_word(word, guessed_letters):
    """Display word with guessed letters revealed"""
    display = []
    for letter in word:
        if letter in guessed_letters:
            display.append(letter)
        else:
            display.append("_")
    return " ".join(display)

def get_valid_letter(guessed_letters):
    """Get valid letter input from user"""
    while True:
        letter = input("Guess a letter: ").strip().lower()
        if len(letter) != 1:
            print("Please enter exactly one character!")
        elif letter not in string.ascii_lowercase:
            print("Please enter a valid English letter!")
        elif letter in guessed_letters:
            print("You've already guessed that letter!")
        else:
            return letter

def select_difficulty():
    """Let player select difficulty level"""
    print("\nDifficulty Levels:")
    print("1. Easy (short words)")
    print("2. Medium (medium-length words)")
    print("3. Hard (long words)")
    
    while True:
        try:
            choice = int(input("Select difficulty (1-3): "))
            if 1 <= choice <= 3:
                return Difficulty(choice)
            print("Please enter a number between 1 and 3!")
        except ValueError:
            print("Please enter a valid number!")

def play_again():
    """Ask player if they want to play again"""
    while True:
        choice = input("\nWould you like to play again? (yes/no): ").strip().lower()
        if choice in ["yes", "y"]:
            return True
        elif choice in ["no", "n"]:
            return False
        print("Please enter 'yes' or 'no'!")

def main():
    print("""
    🎮 Welcome to Hangman! 🎮
    -------------------------
    Guess the letters to reveal the word before the hangman is complete!
    """)
    
    while True:
        difficulty = select_difficulty()
        word = load_words(difficulty)
        guessed_letters = set()
        tries = 6
        correct_letters = set(word)
        
        print(f"\nGame started! The word has {len(word)} letters.")
        
        while tries > 0:
            print(display_hangman(tries))
            current_display = display_word(word, guessed_letters)
            print(f"\nWord: {current_display}")
            print(f"Guessed letters: {' '.join(sorted(guessed_letters))}")
            print(f"Tries remaining: {tries}")
            
            letter = get_valid_letter(guessed_letters)
            guessed_letters.add(letter)
            
            if letter in word:
                print("\n✅ Correct! This letter is in the word.")
                if correct_letters.issubset(guessed_letters):
                    print(f"\n🎉 You won! The word was: {word}")
                    break
            else:
                print("\n❌ Wrong! This letter is not in the word.")
                tries -= 1
        
        if tries == 0:
            print(display_hangman(tries))
            print(f"\n💀 Game over! The word was: {word}")
        
        if not play_again():
            print("\nThanks for playing! Goodbye 👋")
            break

if __name__ == "__main__":
    main()