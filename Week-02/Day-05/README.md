# 📌 Overview

Today's project brought together everything learned throughout Week 2 by building a menu-driven **Student Management System**. The application allows users to manage student records using a nested dictionary data structure and modular programming.

This project strengthened my understanding of program design, data structures, and organizing larger Python applications into reusable functions.

---

## 🎯 Project Objectives

The Student Management System allows users to:

* Add new students
* Remove existing students
* Search for students by Student ID
* Display all student records
* Exit the program safely

---

## 🗂 Data Structure

The project uses a **nested dictionary**, where each Student ID is the key and the student's information is stored as another dictionary.

Example:

```python
students = {
    "ST001": {
        "name": "Justice",
        "surname": "Bishop",
        "score": 95,
        "course": "Python"
    }
}
```

This structure provides fast searching, updating, and removal of student records.

---

## 🛠 Functions Implemented

* `add_student()` – Adds one or more students to the system.
* `remove_student()` – Removes a student using their Student ID.
* `search_student()` – Searches for a student by Student ID.
* `display_students()` – Displays all student records.
* `main()` – Controls the application's menu and program flow.

---

## 💡 Concepts Practiced

* Functions
* Lists
* Dictionaries
* Nested Dictionaries
* Loops
* Conditional Statements
* Menu-driven Programs
* Input Validation
* Searching
* Deleting Dictionary Entries
* Program Design
* Modular Programming

---

## 🚀 Features

* Add multiple students in one session.
* Store student information using nested dictionaries.
* Search students quickly using their unique Student ID.
* Remove students safely from the system.
* Display all student records in a readable format.
* Continue running until the user chooses to exit.

---

## 📚 Lessons Learned

While building this project, I learned:

* How nested dictionaries organize complex data.
* Why unique IDs are better than names for identifying records.
* How to build menu-driven applications using loops and functions.
* The importance of breaking programs into small, reusable functions.
* How program design simplifies implementation before coding begins.

---

## 🔮 Possible Improvements

Future versions of this project could include:

* Update student information.
* Prevent duplicate Student IDs.
* Validate all user input.
* Sort student records alphabetically.
* Calculate class averages and highest scores.
* Save student records to a file.
* Load saved records automatically when the program starts.
