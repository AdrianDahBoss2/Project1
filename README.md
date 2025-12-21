# Kresge Digital Library
#### Description:

A digital interpretation of Kresge Libary in Python.

This program prints a menu for the user to select using the command-line from adding or deleting a book, searching a book, or borrowing or returning a book. Book data is stored in JSON format.

The program requires a file called "catalog.txt" with a pre-installed catalog of books:

[
    {
        "title": "Pride and Prejudice",
        "author": "Jane Austen",
        "year": 1813,
        "available": true
    },
    {
        "title": "The Catcher in the Rye",
        "author": "J.D. Salinger",
        "year": 1951,
        "available": true
    },
    {
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "year": 1960,
        "available": true
    }
]

## Usage:

python kresge_library.py

When the program starts, this menu is printed:
1. Add Book
2. Delete Book
3. Search
4. Check out
5. Return
6. Save and Exit (Ctrl + D)

The user may type "back" (case insensitive) at certain prompts to return to the main menu.

To exit the program safely and save changes, press Ctrl + D.

## Notes:

- Only one book can be borrowed at a time
- The program assumes "catalog.txt" exists and contains valid JSON
- All interactions occur through the command-line
