# # Reverse the sentence

def reverse_sentence(sentence):
    """Reverse the order of words in a sentence"""
    words = sentence.split()
    return ' '.join(reversed(words))  # Using reversed() for better readability

def main():
    print("\n🔤 Sentence Reverser 🔤")
    
    while True:
        sentence = input("\nEnter a sentence (or 'q' to quit): ").strip()
        
        if sentence.lower() == 'q':
            print("\n👋 Exiting the program. Goodbye!")
            break
            
        if not sentence:
            print("⚠ You didn't enter anything. Please try again.")
            continue
            
        reversed_sentence = reverse_sentence(sentence)
        print(f"\nReversed sentence: {reversed_sentence}")
        
        # Optional: Show word count
        print(f"(Original sentence had {len(sentence.split())} words)")

if __name__ == "__main__":
    main()


# Rewrite the sentence

# import string

# def remove_punctuation(text):
#     """Remove all punctuation marks from text"""
#     # Create a translation table to remove punctuation
#     translator = str.maketrans('', '', string.punctuation)
#     return text.translate(translator)

# def get_clean_input(prompt):
#     """Get input from user and validate it"""
#     while True:
#         user_input = input(prompt).strip()
#         if user_input:
#             return user_input
#         print("⚠ Empty input. Please enter a sentence.")

# def main():
#     print("\n🧹 Sentence Cleaner - Punctuation Remover 🧹")
#     print("------------------------------------------")
    
#     sentence = get_clean_input("\nEnter a sentence: ")
#     cleaned = remove_punctuation(sentence)
    
#     print("\nOriginal sentence:", sentence)
#     print("Cleaned sentence:", cleaned)
    
#     # Additional stats
#     punctuation_count = sum(1 for char in sentence if char in string.punctuation)
#     print(f"\nℹ Removed {punctuation_count} punctuation mark{'s' if punctuation_count != 1 else ''}")
#     print(f"ℹ Final length: {len(cleaned)} characters (was {len(sentence)})")

# if __name__ == "__main__":
#     main()