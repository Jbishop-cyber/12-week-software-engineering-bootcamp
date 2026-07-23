# Library Management System - Program Design

## Data Structure

The program will use a **nested dictionary** to store information about each book.

Example:

```python
books = {
    "Giants": {
        "genre": "Sci-Fi",
        "author": "John Doe",
        "year": 2025,
        "available": True
    }
}
```

Each book title acts as the key, while the value is another dictionary containing the book's details.

---

## Functions

```text
add_book()
borrow_book()
return_book()
search_book()
display_books()
```

Each function performs a single responsibility:

* **add_book()** – Add a new book to the library.
* **borrow_book()** – Allow a user to borrow a book if it is available.
* **return_book()** – Mark a borrowed book as available again.
* **search_book()** – Search for books by title or genre.
* **display_books()** – Display all books in alphabetical order.

---

## Algorithm (Pseudocode)

```text
BEGIN

Create an empty library dictionary.

WHILE True

    Display menu:

        1. Add Book
        2. Borrow Book
        3. Return Book
        4. Search Book
        5. Display All Books
        6. Exit

    Ask the user to choose an option.

    IF choice == 1
        Call add_book()

    ELSE IF choice == 2
        Call borrow_book()

    ELSE IF choice == 3
        Call return_book()

    ELSE IF choice == 4
        Call search_book()

    ELSE IF choice == 5
        Call display_books()

    ELSE IF choice == 6
        Display "Goodbye!"
        Exit the program

    ELSE
        Display "Invalid option. Please try again."

END WHILE

END
```

---

## Validation Rules

* Ensure book titles are not empty.
* Ensure the publication year is a valid number.
* Prevent duplicate book titles from being added.
* Validate menu selections.
* Validate all numeric inputs.

---

## Business Rules

* A book that has already been borrowed cannot be borrowed again until it is returned.
* A returned book becomes available for borrowing again.
* Books should be displayed in alphabetical order.
* Users can search by:

  * Full book title
  * Partial title (first few letters)
  * Genre
* If a book is not found, display an appropriate message.

---

## Expected Outcome

The Library Management System should allow users to manage a collection of books efficiently by adding, borrowing, returning, searching, and displaying books while maintaining accurate availability information.
