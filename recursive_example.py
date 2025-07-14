### Recursive Function Example ###

### This function removes consecutive duplicate characters from a word ###

def clean_word(word):
    # Base case: if the word has only one character, return it
    if len(word) == 1:
        return word

    # If the first character is the same as the second, skip the first and call the function recursively
    if word[0] == word[1]:
        return clean_word(word[1:])

    # Otherwise, keep the first character and apply the function to the rest of the word
    return word[0] + clean_word(word[1:])

print(clean_word("wwwoorrlld"))  # Output: world