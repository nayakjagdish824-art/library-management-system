Library Inventory System (Python OOP Project)

Course: Programming for Problem Solving Using Python
Course Code: ETCCPP171
Program: MCA (AI & ML)
Semester: I
Faculty: Ms. Neha Kaushik
Assignment Number: 03

Project Overview

This project is a Python-based Library Inventory System developed using Object-Oriented Programming (OOP) concepts.
It simulates real-world library operations such as:

Adding books

Registering members

Borrowing and returning books

Storing data in JSON files

Viewing library analytics

Running an interactive menu

The system uses:

Classes (Book, Member, Library)

File persistence

Modular code structure

Basic analytics using class-level data

Project Structure
library_system/
│
├── book.py
├── member.py
├── library.py
├── main.py
├── books.json
├── members.json
└── README.md

Features Implemented
Book Management

Create books with title, author, ISBN

Borrow and return functionality

Track availability

Member Management

Register members

Members can borrow and return books

Track borrowed books

Library Operations

Add books

Register members

Lend books using member ID and ISBN

Take book returns

Data Persistence

All books and members are saved in JSON files

Automatically loads saved data when the system starts

Includes error handling for missing or corrupted files

Analytics (Mini Report)

Provides total number of books currently borrowed
(Or "Most Borrowed Book" if implemented)

Bonus: Interactive Console Menu

Includes the following options:

1. Add Book
2. Register Member
3. Borrow Book
4. Return Book
5. View Library Report
6. Exit

How to Run the Program
Step 1: Open Terminal or VS Code

Navigate to the project folder:

cd library_system

Step 2: Run the main file
python main.py

Step 3: Use the menu

Example:

Enter choice: 1
Enter Book Title: Atomic Habits
Enter Author: James Clear
Enter ISBN: 12345

Data Files (Generated Automatically)
books.json example:
[
  {
    "title": "Atomic Habits",
    "author": "James Clear",
    "isbn": "12345",
    "available": true
  }
]

members.json example:
[
  {
    "name": "Rahul",
    "member_id": "M01",
    "borrowed_books": ["12345"]
  }
]

Technologies Used

Python 3

Object-Oriented Programming

File Handling

JSON Module

Modular Programming

Student Information

Name: (Your Name)
Program: MCA (AI & ML)
Assignment: 03 – Library Inventory System