# Library catalogue

import os
import json
from datetime import datetime
from enum import Enum, auto

class BookStatus(Enum):
    AVAILABLE = auto()
    CHECKED_OUT = auto()
    LOST = auto()
    REMOVED = auto()

class Book:
    def _init_(self, isbn, title, author, publication_year, status=BookStatus.AVAILABLE):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.status = status
        self.checkout_history = []
        self.date_added = datetime.now().date()
    
    def check_out(self, borrower_name):
        if self.status != BookStatus.AVAILABLE:
            return False
        
        self.status = BookStatus.CHECKED_OUT
        self.checkout_history.append({
            'borrower': borrower_name,
            'checkout_date': datetime.now().date(),
            'return_date': None
        })
        return True
    
    def check_in(self):
        if self.status != BookStatus.CHECKED_OUT:
            return False
        
        self.status = BookStatus.AVAILABLE
        self.checkout_history[-1]['return_date'] = datetime.now().date()
        return True
    
    def mark_lost(self):
        self.status = BookStatus.LOST
    
    def remove_copy(self):
        self.status = BookStatus.REMOVED
    
    def to_dict(self):
        return {
            'isbn': self.isbn,
            'title': self.title,
            'author': self.author,
            'publication_year': self.publication_year,
            'status': self.status.name,
            'date_added': self.date_added.strftime('%Y-%m-%d'),
            'checkout_history': self.checkout_history
        }

class LibraryCatalog:
    def _init_(self):
        self.books = {}
        self.load_data()
    
    def add_book(self, book):
        if book.isbn in self.books:
            print(f"⚠ Book with ISBN {book.isbn} already exists!")
            return False
        self.books[book.isbn] = book
        print(f"✅ Added '{book.title}' to the catalog")
        return True
    
    def find_book(self, isbn):
        return self.books.get(isbn)
    
    def search_books(self, search_term):
        results = []
        search_term = search_term.lower()
        for book in self.books.values():
            if (search_term in book.title.lower() or 
                search_term in book.author.lower() or 
                search_term == book.isbn):
                results.append(book)
        return results
    
    def save_data(self):
        data = {isbn: book.to_dict() for isbn, book in self.books.items()}
        with open('library_data.json', 'w') as f:
            json.dump(data, f, indent=2)
    
    def load_data(self):
        try:
            with open('library_data.json', 'r') as f:
                data = json.load(f)
                for isbn, book_data in data.items():
                    book = Book(
                        isbn=book_data['isbn'],
                        title=book_data['title'],
                        author=book_data['author'],
                        publication_year=book_data['publication_year'],
                        status=BookStatus[book_data['status']]
                    )
                    book.date_added = datetime.strptime(book_data['date_added'], '%Y-%m-%d').date()
                    book.checkout_history = book_data['checkout_history']
                    self.books[isbn] = book
        except FileNotFoundError:
            pass

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_menu():
    print("\n📚 Library Catalog System")
    print("1. Add a new book")
    print("2. Search for books")
    print("3. Check out a book")
    print("4. Check in a book")
    print("5. Report lost book")
    print("6. Remove book copy")
    print("7. View all books")
    print("8. Exit")

def get_valid_input(prompt, input_type=str, validation_func=None):
    while True:
        try:
            user_input = input(prompt).strip()
            if not user_input:
                raise ValueError("Input cannot be empty")
            
            if input_type == int:
                user_input = int(user_input)
            
            if validation_func and not validation_func(user_input):
                raise ValueError("Invalid input")
            
            return user_input
        except ValueError as e:
            print(f"❌ Error: {e}")

def main():
    catalog = LibraryCatalog()
    
    while True:
        clear_screen()
        display_menu()
        choice = get_valid_input("Enter your choice (1-8): ", int, lambda x: 1 <= x <= 8)
        
        if choice == 1:
            clear_screen()
            print("➕ Add New Book")
            isbn = get_valid_input("ISBN (13 digits): ", str, lambda x: len(x) == 13 and x.isdigit())
            title = get_valid_input("Title: ")
            author = get_valid_input("Author: ")
            year = get_valid_input("Publication year: ", int, lambda x: 1000 <= x <= datetime.now().year)
            
            book = Book(isbn, title, author, year)
            catalog.add_book(book)
        
        elif choice == 2:
            clear_screen()
            print("🔍 Search Books")
            term = get_valid_input("Enter search term (title, author, or ISBN): ")
            results = catalog.search_books(term)
            
            if not results:
                print("\nNo matching books found")
            else:
                print(f"\nFound {len(results)} matching book(s):")
                for book in results:
                    print(f"\nISBN: {book.isbn}")
                    print(f"Title: {book.title}")
                    print(f"Author: {book.author}")
                    print(f"Status: {book.status.name}")
                    print(f"Year: {book.publication_year}")
            
            input("\nPress Enter to continue...")
        
        elif choice == 3:
            clear_screen()
            print("📖 Check Out Book")
            isbn = get_valid_input("Enter ISBN: ")
            book = catalog.find_book(isbn)
            
            if book:
                borrower = get_valid_input("Borrower name: ")
                if book.check_out(borrower):
                    print(f"\n✅ '{book.title}' checked out to {borrower}")
                else:
                    print(f"\n❌ Book is not available for checkout (Status: {book.status.name})")
            else:
                print("\n❌ Book not found")
            
            input("\nPress Enter to continue...")
        
        elif choice == 4:
            clear_screen()
            print("📗 Check In Book")
            isbn = get_valid_input("Enter ISBN: ")
            book = catalog.find_book(isbn)
            
            if book:
                if book.check_in():
                    print(f"\n✅ '{book.title}' checked in successfully")
                else:
                    print(f"\n❌ Book cannot be checked in (Status: {book.status.name})")
            else:
                print("\n❌ Book not found")
            
            input("\nPress Enter to continue...")
        
        elif choice == 5:
            clear_screen()
            print("⚠ Report Lost Book")
            isbn = get_valid_input("Enter ISBN: ")
            book = catalog.find_book(isbn)
            
            if book:
                book.mark_lost()
                print(f"\n✅ '{book.title}' marked as lost")
            else:
                print("\n❌ Book not found")
            
            input("\nPress Enter to continue...")
        
        elif choice == 6:
            clear_screen()
            print("🗑 Remove Book Copy")
            isbn = get_valid_input("Enter ISBN: ")
            book = catalog.find_book(isbn)
            
            if book:
                book.remove_copy()
                print(f"\n✅ '{book.title}' removed from circulation")
            else:
                print("\n❌ Book not found")
            
            input("\nPress Enter to continue...")
        
        elif choice == 7:
            clear_screen()
            print("📚 All Books in Catalog")
            if not catalog.books:
                print("\nNo books in catalog")
            else:
                for book in catalog.books.values():
                    print(f"\nISBN: {book.isbn}")
                    print(f"Title: {book.title}")
                    print(f"Author: {book.author}")
                    print(f"Year: {book.publication_year}")
                    print(f"Status: {book.status.name}")
                    print(f"Added: {book.date_added}")
                    if book.checkout_history:
                        print(f"Last checkout: {book.checkout_history[-1]['borrower']} on {book.checkout_history[-1]['checkout_date']}")
            
            input("\nPress Enter to continue...")
        
        elif choice == 8:
            catalog.save_data()
            print("\n💾 Data saved. Goodbye!")
            break

if __name__ == "__main__":
    main()