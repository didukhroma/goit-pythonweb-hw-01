from abc import ABC, abstractmethod
from typing import Self
from logger import logger


class Book:
    """Base implementation for Book class"""

    def __init__(self: Self, title: str, author: str, year: str):
        """
        Args:
        title (str): Title of the book.
        author (str): Author of the book.
        year (str): Year of the book.

        """
        self.title = title
        self.author = author
        self.year = year

    def __str__(self: Self):
        "String representation of book"
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}"


class LibraryInterface(ABC):
    """Abstract class for library interface"""

    @abstractmethod
    def add_book(self: Self, title: str, author: str, year: str) -> str:
        """Abstract add book method"""

    @abstractmethod
    def remove_book(self: Self, title: str) -> str:
        """Abstract remove book method"""

    @abstractmethod
    def show_books(
        self: Self,
    ) -> None:
        """Abstract show books method"""


class Library(LibraryInterface):
    """Library interface implementation"""

    def __init__(self):
        self.books: list[Book] = []

    def add_book(self: Self, title: str, author: str, year: str) -> str:
        """Library add book implementation"""
        book = Book(title, author, year)
        self.books.append(book)
        return f"Book {title} successfully added"

    def remove_book(self: Self, title: str) -> str:
        """Library remove book implementation"""
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                return f"Book {title} successfully removed"
        return f"Book {title} not found"

    def show_books(
        self: Self,
    ):
        """Library show books implementation"""
        for book in self.books:
            logger(str(book))


class LibraryManager:
    """Library manager implementation"""

    def __init__(self: Self, library: LibraryInterface):
        """Library manager implementation"""
        self.library = library

    def add_book(self: Self, title: str, author: str, year: str):
        """Add book implementation"""
        response = self.library.add_book(title, author, year)
        logger(response)

    def remove_book(
        self: Self,
        title: str,
    ):
        """Remove book implementation"""
        response = self.library.remove_book(title)
        logger(response)

    def show_books(self: Self):
        """Show books implementation"""
        self.library.show_books()


def main():
    """Main function"""
    library = Library()
    manager = LibraryManager(library)

    while True:
        command = input("Enter command (add, remove, show, exit): ").strip().lower()

        match command:
            case "add":
                title = input("Enter book title: ").strip()
                author = input("Enter book author: ").strip()
                year = input("Enter book year: ").strip()
                manager.add_book(title, author, year)
            case "remove":
                title = input("Enter book title to remove: ").strip()
                manager.remove_book(title)
            case "show":
                manager.show_books()
            case "exit":
                break
            case _:
                logger("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
