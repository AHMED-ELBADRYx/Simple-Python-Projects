# Library Manager

books = []
wishlist = []

def clean_input(prompt):
    return input(prompt).strip()

# Add owned books
print("=== Add Books You Own ===")
for i in range(2):
    book = clean_input(f"Enter book #{i+1} you own (or press Enter to skip): ")
    if book:
        books.append(book)

print(f"\n📚 Your Library: {books or 'No books yet'}")

# Add wishlist books
print("\n=== Add Books to Wishlist ===")
for i in range(2):
    book = clean_input(f"Enter book #{i+1} you wish to have (or press Enter to skip): ")
    if book:
        wishlist.append(book)

print(f"\n⭐ Your Wishlist: {wishlist or 'No books in wishlist'}")

# Acquired book
acquired = clean_input("\n=== Acquired Book ===\nEnter a book from your wishlist that you've acquired (or press Enter to skip): ")
if acquired and acquired in wishlist:
    books.append(acquired)
    wishlist.remove(acquired)
    print(f"\n✅ '{acquired}' has been moved to your library!")
elif acquired and acquired not in wishlist:
    print(f"\n❌ '{acquired}' is not in your wishlist.")
else:
    print("\nNo book acquired.")

print(f"Updated Library: {books or 'No books yet'}")
print(f"Updated Wishlist: {wishlist or 'No books in wishlist'}")

# Donate book
donated = clean_input("\n=== Donate Book ===\nEnter a book from your library to donate (or press Enter to skip): ")
if donated and donated in books:
    books.remove(donated)
    print(f"\n✅ '{donated}' has been donated. Thank you!")
elif donated and donated not in books:
    print(f"\n❌ '{donated}' is not in your library.")
else:
    print("\nNo book donated.")

print(f"\nFinal Library after Donations: {books or 'No books remaining'}")
print(f"Final Wishlist: {wishlist or 'No books in wishlist'}")