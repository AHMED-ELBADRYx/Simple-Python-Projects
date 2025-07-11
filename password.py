# Write a password

import random
import string
import sys

def get_valid_input(prompt, min_val=0, max_val=50):
    """Get and validate user input as positive integer within range"""
    while True:
        try:
            value = int(input(prompt))
            if min_val <= value <= max_val:
                return value
            print(f"⚠ Please enter a number between {min_val} and {max_val}")
        except ValueError:
            print("⚠ Invalid input. Please enter a whole number.")

def validate_password_requirements(total, letters, symbols, digits):
    """Validate that the components add up to the total length"""
    if letters + symbols + digits != total:
        print(f"❌ Error: {letters} (letters) + {symbols} (symbols) + {digits} (digits) "
              f"= {letters+symbols+digits} ≠ {total} (total)")
        return False
    if total < 8:
        print("⚠ Warning: For security, we recommend passwords of at least 8 characters")
    return True

def generate_password(letters, symbols, digits):
    """Generate a secure password with specified composition"""
    # Create character pools
    letter_pool = string.ascii_letters
    symbol_pool = string.punctuation.replace('"', '').replace("'", "")  # Remove problematic quotes
    digit_pool = string.digits
    
    # Generate components
    password_chars = (
        random.choices(letter_pool, k=letters) +
        random.choices(symbol_pool, k=symbols) +
        random.choices(digit_pool, k=digits)
    )
    
    # Ensure randomness
    random.SystemRandom().shuffle(password_chars)
    return ''.join(password_chars)

def main():
    print("\n🔐 Secure Password Generator 🔐")
    print("----------------------------")
    
    # Get user input with validation
    total = get_valid_input("\nEnter total password length (8-50 recommended): ", 1, 100)
    letters = get_valid_input("Number of letters: ", 0, total)
    symbols = get_valid_input("Number of symbols: ", 0, total)
    digits = get_valid_input("Number of digits: ", 0, total)
    
    # Validate requirements
    if not validate_password_requirements(total, letters, symbols, digits):
        sys.exit("💥 Password generation failed due to invalid requirements")
    
    # Generate and display password
    password = generate_password(letters, symbols, digits)
    print(f"\n🔒 Generated Password: {password}")
    print(f"📊 Composition: {letters} letters, {symbols} symbols, {digits} digits")
    print("\n⚠ Remember to store this password securely!")

if __name__ == "__main__":
    main()