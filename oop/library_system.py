# library_system.py

# Base class: Book
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Book: {self.title} by {self.author}"


# Derived class: EBook (inherits from Book)
class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)  # Initialize the title and author using the base class
        self.file_size = file_size  # Specific attribute for EBook

    def __str__(self):
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


# Derived class: PrintBook (inherits from Book)
class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)  # Initialize the title and author using the base class
        self.page_count = page_count  # Specific attribute for PrintBook

    def __str__(self):
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


# Composition class: Library
class Library:
    def __init__(self):
        self.books = []  # List to hold Book, EBook, and PrintBook objects

    def add_book(self, book):
        self.books.append(book)  # Add a book to the library collection

    def list_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            for book in self.books:
                print(book)  # Print the string representation of each book (calls __str__)

                
                
from library_system import Book, EBook, PrintBook, Library

def main():
    # Create a Library instance
    my_library = Library()

    # Create instances of each type of book
    classic_book = Book("Pride and Prejudice", "Jane Austen")
    digital_novel = EBook("Snow Crash", "Neal Stephenson", 500)
    paper_novel = PrintBook("The Catcher in the Rye", "J.D. Salinger", 234)

    # Add books to the library
    my_library.add_book(classic_book)
    my_library.add_book(digital_novel)
    my_library.add_book(paper_novel)

    # List all books in the library
    my_library.list_books()

if __name__ == "__main__":
    main()
