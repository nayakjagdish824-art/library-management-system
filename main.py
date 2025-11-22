# main.py
# Author: Jagdish Nayak
# Date: 21-11-2025
# Assignment: Library Inventory System - main interactive menu

from library import Library
from book import Book
from member import Member
import os

DATA_DIR = "."  # files will be created in the same folder (books.json, members.json, borrow_counts.json)

def print_welcome():
    print("=======================================")
    print("  Welcome to the Library Inventory App ")
    print("  Programming for Problem Solving - MCA ")
    print("=======================================\n")

def input_book_details():
    title = input("Enter book title: ").strip()
    author = input("Enter author name: ").strip()
    isbn = input("Enter ISBN (unique): ").strip()
    return title, author, isbn

def input_member_details():
    name = input("Enter member name: ").strip()
    member_id = input("Enter member ID (unique): ").strip()
    return name, member_id

def main_menu(lib: Library):
    while True:
        print("\nMenu:")
        print("1. Add Book")
        print("2. Register Member")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. View Library Report")
        print("6. List Books")
        print("7. List Members")
        print("8. Exit")
        choice = input("Choose an option [1-8]: ").strip()

        if choice == "1":
            title, author, isbn = input_book_details()
            lib.add_book(Book(title, author, isbn))
        elif choice == "2":
            name, member_id = input_member_details()
            lib.register_member(Member(name, member_id))
        elif choice == "3":
            member_id = input("Enter member ID: ").strip()
            isbn = input("Enter ISBN to borrow: ").strip()
            lib.lend_book(member_id, isbn)
        elif choice == "4":
            member_id = input("Enter member ID: ").strip()
            isbn = input("Enter ISBN to return: ").strip()
            lib.take_return(member_id, isbn)
        elif choice == "5":
            lib.print_report()
        elif choice == "6":
            print("Books in library:")
            for b in lib.books.values():
                status = "Available" if b.available else "Borrowed"
                print(f"- {b.title} by {b.author} (ISBN: {b.isbn}) — {status}")
        elif choice == "7":
            print("Registered members:")
            for m in lib.members.values():
                print(f"- {m.name} (ID: {m.member_id}) — Borrowed: {m.borrowed_books}")
        elif choice == "8":
            print("Saving data and exiting. Goodbye!")
            # data saved during operations; just exit
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    print_welcome()
    lib = Library(DATA_DIR)

    # Optionally add some default sample data if library is empty (comment out if not desired)
    if not lib.books and not lib.members:
        # sample books
        lib.add_book(Book("The Alchemist", "Paulo Coelho", "ISBN001"))
        lib.add_book(Book("Introduction to Algorithms", "Cormen et al.", "ISBN002"))
        lib.add_book(Book("Python Crash Course", "Eric Matthes", "ISBN003"))
        # sample members
        lib.register_member(Member("Alice", "M001"))
        lib.register_member(Member("Bob", "M002"))

    main_menu(lib)
