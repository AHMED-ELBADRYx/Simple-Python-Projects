# Verify email entry

import re
import time
from enum import Enum, auto

class ValidationResult(Enum):
    VALID = auto()
    INVALID_FORMAT = auto()
    INVALID_DOMAIN = auto()
    DISPOSABLE = auto()

class EmailValidator:
    # Common email regex pattern
    EMAIL_REGEX = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    # List of common disposable email domains
    DISPOSABLE_DOMAINS = {
        'mailinator.com', 'temp-mail.org', 'guerrillamail.com',
        '10minutemail.com', 'throwawaymail.com', 'yopmail.com'
    }
    
    @classmethod
    def validate_email(cls, email: str) -> ValidationResult:
        """Validate an email address with multiple checks"""
        email = email.strip().lower()
        
        # Basic format validation
        if not re.fullmatch(cls.EMAIL_REGEX, email):
            return ValidationResult.INVALID_FORMAT
            
        # Extract domain
        domain = email.split('@')[1]
        
        # Disposable email check
        if domain in cls.DISPOSABLE_DOMAINS:
            return ValidationResult.DISPOSABLE
            
        # Basic domain validation
        if '.' not in domain or len(domain.split('.')[-1]) < 2:
            return ValidationResult.INVALID_DOMAIN
            
        return ValidationResult.VALID

def animated_loading(message: str, duration: int = 3):
    """Show an animated loading sequence"""
    print(message, end='', flush=True)
    for _ in range(duration):
        time.sleep(0.5)
        print('.', end='', flush=True)
    print()

def get_valid_name() -> str:
    """Get and validate user name"""
    while True:
        name = input("What is your name? ").strip()
        if not name:
            print("❌ Name cannot be empty. Please try again.")
            continue
            
        if any(char.isdigit() for char in name):
            print("❌ Name should not contain numbers. Please try again.")
            continue
            
        if len(name.split()) < 2:
            print("❌ Please enter both first and last name.")
            continue
            
        return name

def get_valid_email() -> str:
    """Get and validate email address"""
    while True:
        email = input("Enter your email: ").strip()
        result = EmailValidator.validate_email(email)
        
        if result == ValidationResult.VALID:
            return email
            
        error_messages = {
            ValidationResult.INVALID_FORMAT: "Invalid email format (should be user@domain.com)",
            ValidationResult.INVALID_DOMAIN: "Invalid domain in email address",
            ValidationResult.DISPOSABLE: "Disposable/temporary emails are not allowed"
        }
        print(f"❌ {error_messages[result]}. Please try again.")

def main():
    print("\n📝 User Registration System")
    print("=" * 30)
    
    # Get validated user input
    name = get_valid_name()
    email = get_valid_email()
    
    # Simulate processing
    animated_loading("\nVerifying your information", 3)
    print("\n✓ Verification complete")
    
    # Display results
    print(f"\n✅ Successfully registered:\nName: {name.title()}\nEmail: {email.lower()}")
    
    # Confirmation
    print("\nThank you for registering!")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠ Registration cancelled by user.")
    except Exception as e:
        print(f"\n❌ An error occurred: {str(e)}")