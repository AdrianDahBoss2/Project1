'''
Authors: Adrian Barno
Last Modified: April 11th
The purpose of this program is to create a digital library that users can add, delete, search, check out, or return books.

A file named 'catalog.txt' is required with the contents of:
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

'''

import json

# Block that brings user back to the main function.
def back():
    while True:
        back = str(input('If you\'d like to go back type \'Back\' otherwise press Enter: \n'))
        if back.lower() == 'back':
            return 'back'
        elif back == '':
            return 'continue'
        else: 
            print('Invalid Input! Try again: ')

# Function for choice 1 (Add a book).
def choice1():
    print('\nYou have selected to add a book')

    # Block that sends the user back if entered 'back'.
    if back() == 'back':
        return

    # Block that recieves information about the book.
    while True:
        title = str(input('Please enter the title of the book: '))
        if not title.strip():
            print('Invalid input! Please enter a title: ')
        else:
            break
    while True:
        author = str(input('Please enter the author of the book: '))
        if not author.strip():
            print('Invalid input! Please enter an author: ')
        else:
            break
    while True:
        try:
            year = int(input('Please enter the date of the book: '))
            if len(str(year)) > 4:
                print('Please enter a valid date!')
            else:
                break
        except ValueError:
            print('Invalid input! Please enter a date: ')

    # Add the new book and its information as a dictionary.
    new_book = {
        "title": title.strip().lower(),
        "author": author.strip().lower(),
        "year": year,
        "available": True
    }
            
    # Block that loads the current catalog.
    with open('catalog.txt', 'r') as f:
        library = json.load(f) # Loads the catalog onto 'library'.

        # Block that checks if the book is already in the catalog.
        if new_book in library:
            print('\nBook is already in the catalog!')
        else:
            library.append(new_book) # Appends the new book to library.
            print(f"\n'{title.capitalize()}' has been added to the catalog!")
            
            # Saves library back to the file
            with open('catalog.txt', 'w') as f:
                json.dump(library, f, indent=4)

# Function for choice 2 (Delete a book).
def choice2():
    print('\nYou have selected to delete a book')
  
    # Block that sends the user back if entered 'back'.
    if back() == 'back':
        return

    # Opens the catalog file.
    with open('catalog.txt', 'r') as f:
        books = json.load(f)

        # Displays the books in the catalog.
        print('\nHere are the books currently available: \n')
        for book in books:
            print(f"{book['title']} by {book['author']} ({book['year']}) - Available: {book['available']}")

    # Block that deletes the book.
    delete = str(input('\nPlease enter the title of the book you\'d like to delete: ')) # Asks for the title of the book to be deleted.
    found = False # Variable that tracks if the book was found.
    library = []
    for book in books:
        if book['title'].lower() == delete.lower():
            found = True
            print(f"\nThe book {book['title']} by {book['author']} was found")

            # Block that asks for confirmation before continuing.
            while True:
                confirmation = input('Are you sure you want to delete this book (y/n): ')
                if confirmation.lower() == 'y':
                    print('The book was successesfully deleted!')
                    break
                elif confirmation.lower() == 'n':
                    print('\nThe deletion was cancelled')
                    library.append(book) # Keeps the book if deletion was cancelled.
                    break
                else:
                    print('Invalid Input! Try again: ')
        else:
            library.append(book) # Always keeps books that do not match.

    # Block that allows user to try again if the book was not found.
    if not found:
        while True:
            confirmation = input(f"\nNo book called '{delete}' was found. Would you like to try again? (y/n) ")
            if confirmation.lower() == 'y':
                choice2()
                break
            elif confirmation.lower() == 'n':
                return
            else:
                print('Invalid Input! Try again: ')
          
    # Saves the changes.
    with open('catalog.txt', 'w') as f:
        json.dump(library, f, indent=4)

# Function for choice 3 (Search catalog).
def choice3():
    print('\nYou have selected to search the catalog')
  
    # Block that sends the user back if entered 'back'.
    if back() == 'back':
        return

    # Opens the catalog file.
    with open('catalog.txt', 'r') as f:
        books = json.load(f)
          
        print('\nHere are the books currently available: \n')
        for book in books:
            print(f"{book['title']} by {book['author']} ({book['year']}) - Available: {book['available']}")
    print('\n')
 

# Function for choice 4 (Check out).
def choice4():
    print('\nYou have selected to check out a book')
    
    # Block that sends the user back if entered 'back'.
    if back() == 'back':
        return

    # Block that loads the current catalog.
    with open('catalog.txt', 'r') as f:
        books = json.load(f)

        # Block that checks if user has already checked out a book.
        for book in books:
            if book['available'] == False:
                print(f"The book {book['title']} by {book['author']} ({book['year']}) is already checked out, if you'd like to check out another book, please return your book!")
                return
                
        # Block that displays the books currently available.
        print('\nHere are the books currently available: \n')
        for book in books:
            if book['available'] == True:
                print(f"{book['title']} by {book['author']} ({book['year']}) - Available: {book['available']}")

    # Block that checks out the book.
    choice = str(input('\nPlease enter the title of the book you\'d like to check out: ')) # Asks for the title of the book to be checked out.
    found = False # Variable that tracks if the book was found.
    for book in books:
        if book['title'].lower() == choice.lower():
            found = True
            if book['available'] == True:
                print(f"\nThe book {book['title']} by {book['author']} was found")
                
                # Block that asks for confirmation before continuing.
                while True:
                    confirmation = input('Are you sure you want to check out this book (y/n): ')
                    if confirmation.lower() == 'y':
                        book['available'] = False
                        print(f"\nThe book {book['title']} was successesfully checked out!")
                        break
                    elif confirmation.lower() == 'n':
                        print('The book was not checked out')
                        return
                    else:
                        print('Invalid Input! Try again: ')
            else:
                print(f"\nSorry, '{book['title']}' is already checked out.")
            
    # Block that allows user to try again if the book was not found.
    if not found:
        while True:
            confirmation = input(f"\nNo book called '{choice}' was found. Would you like to try again? (y/n) ")
            if confirmation.lower() == 'y':
                choice4()
                break
            elif confirmation.lower() == 'n':
                return
            else:
                print('Invalid Input! Try again: ')

    # Saves changes.
    with open('catalog.txt', 'w') as f:
        json.dump(books, f, indent=4)

# Function for choice 5 (Return).
def choice5():
    print('\nYou have selected to return a book')
  
    # Block that sends the user back if entered 'back'.
    if back() == 'back':
        return

    # Opens the catalog file.
    with open('catalog.txt', 'r') as f:
        books = json.load(f)
        if all(book['available'] for book in books):
            print("There are no books to return.")
            return
        else:
            print('\nHere are the books currently checked out: \n')
            for book in books:
                if book['available'] == False:
                    print(f"{book['title']} by {book['author']} ({book['year']}) - Available: {book['available']}")

    # Block that returns the book.
    choice = str(input('\nPlease enter the title of the book you\'d like to return: ')) # Asks for the title of the book to be returned.
    found = False # Variable that tracks if the book was found.
    for book in books:
        if book['title'].lower() == choice.lower():
            found = True
            if book['available'] == False:
                print(f"\nThe book {book['title']} by {book['author']} was found!")
                
                # Block that asks for confirmation before continuing.
                while True:
                    confirmation = input('Are you sure you want to return this book (y/n): ')
                    if confirmation.lower() == 'y':
                        book['available'] = True
                        print(f"\nThe book {book['title']} was successesfully returned!")
                        break
                    elif confirmation.lower() == 'n':
                        print('The book was not returned')
                        return
                    else:
                        print('Invalid Input! Try again: ')
            else:
                print(f"\nSorry, '{book['title']}' is already returned")
            
    # Block that allows user to try again if the book was not found.
    if not found:
        while True:
            confirmation = input(f"\nNo book called '{choice}' was found. Would you like to try again? (y/n) ")
            if confirmation.lower() == 'y':
                choice5()
                break
            elif confirmation.lower() == 'n':
                return
            else:
                print('Invalid Input! Try again: ')

    # Saves changes.
    with open('catalog.txt', 'w') as f:
        json.dump(books, f, indent=4)


# Function for choice 6 (Save and Exit).
def choice6():
    print('Have a great day!')

# Main function.
def main():
    print('Hello, Welcome to Kresge Library!')
    while True:
        print("\n1. Add Book\n2. Delete Book \n3. Search\n4. Check Out\n5. Return\n6. Save and Exit (Press Enter)")
        try: 
            choice = int(input('Enter choice: '))
            if choice == 1:
                choice1()
            elif choice == 2:
                choice2()
            elif choice == 3:
                choice3()
            elif choice == 4:
                choice4()
            elif choice == 5:
                choice5()
            elif choice == 6:
                choice6()
                break
            else:
                print('Invalid input! Please select options 1-6!')
        except ValueError:
            print('Invalid input! Please select options 1-6!')
            
main()
