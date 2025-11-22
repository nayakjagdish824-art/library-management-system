# book.py
# Author: Jagdish Nayak
# Date: 21-11-2025
# Assignment: Library Inventory - Book class

import json

class Book:
    def __init__(self, title: str, author: str, isbn: str, available: bool = True):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = available

    def borrow(self):
        """Mark the book as borrowed (not available)."""
        self.available = False

    def return_book(self):
        """Mark the book as available."""
        self.available = True

    def to_dict(self):
        """For JSON persistence."""
        return {
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "available": self.available
        }

    @staticmethod
    def from_dict(d):
        """Create Book object from dict loaded from JSON."""
        return Book(d["title"], d["author"], d["isbn"], d.get("available", True))
