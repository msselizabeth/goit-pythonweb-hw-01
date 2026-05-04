import logging
from abc import ABC, abstractmethod

# Setup logging
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)


class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year


class LibraryInterface(ABC):
    @abstractmethod
    def add_book(self, book):
        pass

    @abstractmethod
    def remove_book(self, title):
        pass

    @abstractmethod
    def show_books(self):
        pass


class Library(LibraryInterface):
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)  # add the book to the list of Library intance

    def remove_book(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)

    def show_books(self):
        return self.books


class LibraryManager:
    def __init__(self, library):
        self.library = library

    def add_book(self, title, author, year):
        new_book = Book(title, author, year)
        self.library.add_book(new_book)

    def remove_book(self, title):
        self.library.remove_book(title)

    def show_books(self):
        books = self.library.show_books()
        # Check if ther is any books to show
        if not books:
            logger.info("Library is empty!")

        for b in books:
            logger.info(f"Title: {b.title}. Author: {b.author}. Year: {b.year}.")


def main():
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
                logger.warning("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
