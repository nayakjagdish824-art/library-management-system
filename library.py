# library.py
# Author: Jagdish Nayak
# Date: 21-11-2025
# Assignment: Library Inventory - Library logic + persistence + analytics

import json
import os
from book import Book
from member import Member

BOOKS_FILE = "books.json"
MEMBERS_FILE = "members.json"
COUNTS_FILE = "borrow_counts.json"  # tracks how many times each book was borrowed

class Library:
    def __init__(self, data_dir="."):
        # store files in data_dir
        self.data_dir = data_dir
        self.books = {}    # isbn -> Book
        self.members = {}  # member_id -> Member
        self.borrow_counts = {}  # isbn -> int
        self._load_all()

    # ---------- CRUD and actions ----------
    def add_book(self, book: Book):
        if book.isbn in self.books:
            print(f"[Info] Book with ISBN {book.isbn} already exists. Skipping.")
            return
        self.books[book.isbn] = book
        self.borrow_counts.setdefault(book.isbn, 0)
        self._save_books()
        self._save_counts()
        print(f"Book added: {book.title} (ISBN: {book.isbn})")

    def register_member(self, member: Member):
        if member.member_id in self.members:
            print(f"[Info] Member with ID {member.member_id} already exists. Skipping.")
            return
        self.members[member.member_id] = member
        self._save_members()
        print(f"Member registered: {member.name} (ID: {member.member_id})")

    def lend_book(self, member_id: str, isbn: str):
        if member_id not in self.members:
            print("Member not found.")
            return False
        if isbn not in self.books:
            print("Book not found.")
            return False

        member = self.members[member_id]
        book = self.books[isbn]

        if not book.available:
            print(f"Book '{book.title}' is currently not available.")
            return False

        # perform lend
        book.borrow()
        member.borrow_book(isbn)
        self.borrow_counts[isbn] = self.borrow_counts.get(isbn, 0) + 1

        # persist
        self._save_books()
        self._save_members()
        self._save_counts()

        print(f"Book '{book.title}' lent to {member.name}.")
        return True

    def take_return(self, member_id: str, isbn: str):
        if member_id not in self.members:
            print("Member not found.")
            return False
        if isbn not in self.books:
            print("Book not found.")
            return False

        member = self.members[member_id]
        book = self.books[isbn]

        if isbn not in member.borrowed_books:
            print(f"{member.name} did not borrow book with ISBN {isbn}.")
            return False

        book.return_book()
        member.return_book(isbn)

        # persist
        self._save_books()
        self._save_members()
        print(f"Book '{book.title}' returned by {member.name}.")
        return True

    # ---------- Persistence ----------
    def _books_path(self):
        return os.path.join(self.data_dir, BOOKS_FILE)

    def _members_path(self):
        return os.path.join(self.data_dir, MEMBERS_FILE)

    def _counts_path(self):
        return os.path.join(self.data_dir, COUNTS_FILE)

    def _save_books(self):
        data = [b.to_dict() for b in self.books.values()]
        with open(self._books_path(), "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)

    def _save_members(self):
        data = [m.to_dict() for m in self.members.values()]
        with open(self._members_path(), "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)

    def _save_counts(self):
        with open(self._counts_path(), "w", encoding="utf-8") as f:
            json.dump(self.borrow_counts, f, indent=2)

    def _load_all(self):
        # load books
        try:
            with open(self._books_path(), "r", encoding="utf-8") as f:
                data = json.load(f)
                for d in data:
                    b = Book.from_dict(d)
                    self.books[b.isbn] = b
        except FileNotFoundError:
            # no file yet - start fresh
            pass
        except (json.JSONDecodeError, Exception) as e:
            print(f"[Warning] Could not load books file: {e}")

        # load members
        try:
            with open(self._members_path(), "r", encoding="utf-8") as f:
                data = json.load(f)
                for d in data:
                    m = Member.from_dict(d)
                    self.members[m.member_id] = m
        except FileNotFoundError:
            pass
        except (json.JSONDecodeError, Exception) as e:
            print(f"[Warning] Could not load members file: {e}")

        # load counts
        try:
            with open(self._counts_path(), "r", encoding="utf-8") as f:
                self.borrow_counts = json.load(f)
        except FileNotFoundError:
            pass
        except (json.JSONDecodeError, Exception) as e:
            print(f"[Warning] Could not load borrow counts file: {e}")

        # Ensure borrow_counts has keys for existing books
        for isbn in self.books:
            self.borrow_counts.setdefault(isbn, 0)

    # ---------- Simple reporting / analytics ----------
    def most_borrowed_book(self):
        if not self.borrow_counts:
            return None, 0
        isbn = max(self.borrow_counts, key=lambda k: self.borrow_counts[k])
        return self.books.get(isbn), self.borrow_counts[isbn]

    def total_active_members(self):
        """Members who currently have at least one borrowed book"""
        return sum(1 for m in self.members.values() if m.borrowed_books)

    def total_books_currently_borrowed(self):
        """Count of books currently borrowed (i.e., available == False)"""
        return sum(1 for b in self.books.values() if not b.available)

    def print_report(self):
        print("---- Library Report ----")
        total_books = len(self.books)
        total_members = len(self.members)
        currently_borrowed = self.total_books_currently_borrowed()
        active_members = self.total_active_members()
        print(f"Total books: {total_books}")
        print(f"Total registered members: {total_members}")
        print(f"Books currently borrowed: {currently_borrowed}")
        print(f"Active members (with borrowed books): {active_members}")

        book, count = self.most_borrowed_book()
        if book:
            print(f"Most borrowed book: '{book.title}' (ISBN: {book.isbn}) — borrowed {count} times")
        else:
            print("Most borrowed book: None")
        print("------------------------")
