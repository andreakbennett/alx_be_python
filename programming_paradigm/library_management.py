#!/usr/bin/env/python3
class Book:
    def __init__(self, title, author):
        """Initialize a Book instance with a title, an author, and its availability status."""
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        """Marks the book as checked out if it's not already checked out."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Marks the book as returned (available)."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """Returns True if the book is available (not checked out), otherwise False."""
        return not self._is_checked_out


class Library:
    def __init__(self):
        """Initialize a Library instance with an empty list of books."""
        self._books = []

    def add_book(self, book):
        """Adds a Book instance to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Attempts to check out a book by its title."""
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                print(f"'{title}' has been checked out.")
                return
        print(f"'{title}' is not available for check out.")

    def return_book(self, title):
        """Attempts to return a book by its title."""
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                print(f"'{title}' has been returned.")
                return
        print(f"'{title}' is not currently checked out.")

    def list_available_books(self):
        """Prints a list of available books."""
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            for book in available_books:
                print(f"{book.title} by {book.author}")
        else:
            print("No books available.")

