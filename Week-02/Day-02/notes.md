## Searching Through a List

Searching means checking each element in a list until the required item is found.

Example:

```python
students = ["Justice", "Ada", "John"]

for student in students:
    if student == "Ada":
        print("Student found!")
```

## Searching with an Index

Sometimes we need to know where an item is located.

```python
students = ["Justice", "Ada", "John"]

for i in range(len(students)):
    if students[i] == "Ada":
        print(i)
```

Output:

```
1
```

## Flag Variables

A flag variable keeps track of whether something has happened.

Example:

```python
found = False

for student in students:
    if student == "Ada":
        found = True

if found:
    print("Student exists.")
else:
    print("Student not found.")
```

## The break Statement

`break` immediately stops a loop.

Example:

```python
for student in students:
    if student == "Ada":
        print("Found")
        break
```

This prevents unnecessary comparisons after the item has been found.


## Counting Occurrences

Sometimes we need to count how many times an item appears.

Example:

```python
count = 0

for number in numbers:
    if number == target:
        count += 1
```

## Finding the Largest Value

Algorithm:

1. Assume the first element is the largest.
2. Compare every other element.
3. Update the largest value whenever a bigger one is found.
4. Return the largest value.

---

## Searching vs Counting

Searching:

* Stops once the item is found.
* Uses `break` or `return`.

Counting:

* Continues through the whole list.
* Counts every occurrence.

## Input Validation

Never trust user input.

Example:

```python
while name == "":
    name = input("Enter a valid name: ")
```

## strip()

`strip()` removes spaces from the beginning and end of a string.

Example:

```python
name = input("Enter name: ").strip()
```

This helps reject blank input such as:

```
""
" "
"     "
```

## Mini Project

Student Search System

Features:

* Store student names
* Display all students
* Display first and last student
* Search for a student
* Display the student's index
* Search repeatedly until the user exits

## Key Concepts Learned

* Lists
* Searching
* Indexes
* Flag variables
* break
* while loops
* Input validation
* strip()
* Function decomposition

## Things to Remember

* A list (`[]`) is different from an empty string (`""`).
* `" "` (spaces) is not an empty string.
* `strip()` removes leading and trailing spaces.
* Use `break` when you no longer need to continue searching.
* Use a flag variable when you need to remember whether something was found.
* Keep functions focused on one responsibility.