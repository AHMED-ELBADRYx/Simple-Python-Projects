# Writing the binary name as two letters 

def get_names():
    """Get comma-separated names from user"""
    while True:
        names_input = input("Enter first and last names separated by commas (e.g., John Doe, Jane Smith): ").strip()
        if names_input:
            return [name.strip() for name in names_input.split(",") if name.strip()]
        print("⚠ Error: No names entered. Please try again.")

def create_abbreviations(names_list):
    """Generate name abbreviations"""
    abbreviations = []
    for full_name in names_list:
        parts = full_name.split()
        if len(parts) >= 2:
            first_letter = parts[0][0].upper()
            last_letter = parts[-1][0].upper()  # Using [-1] to get last part
            abbreviations.append(f"{first_letter}.{last_letter}.")
        else:
            print(f"⚠ Warning: '{full_name}' is missing a last name. Skipped.")
    return abbreviations

def display_results(abbreviations):
    """Display the generated abbreviations"""
    print("\n📋 Name Abbreviations:")
    if abbreviations:
        for abbr in abbreviations:
            print(abbr)
    else:
        print("No valid abbreviations were generated.")

def main():
    print("\n🌟 Name Abbreviator 🌟")
    
    # Get names from user
    names_list = get_names()
    
    # Generate abbreviations
    abbreviations = create_abbreviations(names_list)
    
    # Display results
    display_results(abbreviations)
    
    print("\n✅ Process completed!")

if __name__ == "__main__":
    main()