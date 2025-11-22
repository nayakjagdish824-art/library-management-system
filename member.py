# member.py
# Author: Jagdish Nayak
# Date: 21-11-2025
# Assignment: Library Inventory - Member class

class Member:
    def __init__(self, name: str, member_id: str):
        self.name = name
        self.member_id = member_id
        # store isbn strings of borrowed books
        self.borrowed_books = []

    def borrow_book(self, isbn: str):
        """Record that the member borrowed a book (isbn)."""
        if isbn not in self.borrowed_books:
            self.borrowed_books.append(isbn)

    def return_book(self, isbn: str):
        """Remove isbn from borrowed list if present."""
        if isbn in self.borrowed_books:
            self.borrowed_books.remove(isbn)

    def list_books(self):
        """Return the list of borrowed ISBNs."""
        return list(self.borrowed_books)

    def to_dict(self):
        """For JSON persistence."""
        return {
            "name": self.name,
            "member_id": self.member_id,
            "borrowed_books": self.borrowed_books
        }

    @staticmethod
    def from_dict(d):
        m = Member(d["name"], d["member_id"])
        m.borrowed_books = d.get("borrowed_books", [])
        return m
