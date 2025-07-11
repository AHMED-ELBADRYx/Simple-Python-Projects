# Sentence encryption

import string
from enum import Enum

class EncryptionMode(Enum):
    ENCRYPT = 1
    DECRYPT = 2

class CaesarCipher:
    def __init__(self):
        self.lower_alpha = string.ascii_lowercase
        self.upper_alpha = string.ascii_uppercase
        self.digits = string.digits
        self.symbols = string.punctuation + " "

    def get_valid_input(self, prompt, input_type=str):
        """Get and validate user input"""
        while True:
            try:
                user_input = input(prompt).strip()
                if not user_input:
                    raise ValueError("Input cannot be empty")
                if input_type == int:
                    return int(user_input)
                return user_input
            except ValueError as e:
                print(f"❌ Invalid input: {e}")

    def transform_char(self, char, steps, mode):
        """Transform a single character based on mode"""
        if char in self.lower_alpha:
            alphabet = self.lower_alpha
        elif char in self.upper_alpha:
            alphabet = self.upper_alpha
        elif char in self.digits:
            alphabet = self.digits
        else:
            return char  # Leave symbols and spaces unchanged

        index = alphabet.index(char)
        if mode == EncryptionMode.ENCRYPT:
            new_index = (index + steps) % len(alphabet)
        else:  # DECRYPT
            new_index = (index - steps) % len(alphabet)
        return alphabet[new_index]

    def process_text(self, text, steps, mode):
        """Process entire text with given steps and mode"""
        return ''.join([self.transform_char(char, steps, mode) for char in text])

    def run(self):
        """Main program interface"""
        print("🔐 Advanced Caesar Cipher Tool 🔐")
        print("="*40)
        
        while True:
            print("\nOptions:")
            print("1. Encrypt text")
            print("2. Decrypt text")
            print("3. Exit")
            
            choice = self.get_valid_input("Select option (1-3): ", int)
            
            if choice == 3:
                print("\n👋 Thank you for using the encryption tool!")
                break
            elif choice not in [1, 2]:
                print("⚠ Please select a valid option (1-3)")
                continue
                
            mode = EncryptionMode(choice)
            text = self.get_valid_input(f"\nEnter text to {mode.name.lower()}: ")
            steps = self.get_valid_input("Enter number of steps (shift value): ", int)
            
            result = self.process_text(text, steps, mode)
            print(f"\n🔮 {'Encrypted' if mode == EncryptionMode.ENCRYPT else 'Decrypted'} text:")
            print("="*40)
            print(result)
            print("="*40)

if __name__ == "__main__":
    cipher = CaesarCipher()
    cipher.run()