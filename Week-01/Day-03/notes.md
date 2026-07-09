# Week 1 - Day 3 Notes

# Conditional Statements (`if`, `elif`, `else`)

Conditional statements allow a program to make decisions based on whether a condition is **True** or **False**. Instead of executing every line of code, the program chooses which block of code to run.

Examples of where conditional statements are used:

* Checking if a user is old enough to vote.
* Verifying a password.
* Calculating a student's grade.
* Determining whether a number is even or odd.

---

## `if` Statement

An `if` statement executes a block of code only when its condition is `True`.

### Syntax

```python
if condition:
    # code to execute
```

### Example

```python
age = 20

if age >= 18:
    print("You are an adult.")
```

If the condition is `False`, Python skips the indented block.

---

## `if...else`

Use `if...else` when there are two possible outcomes.

### Example

```python
age = 16

if age >= 18:
    print("You can vote.")
else:
    print("You cannot vote yet.")
```

---

## `if...elif...else`

Use `elif` when there are multiple conditions to check.

Python checks the conditions from **top to bottom**. As soon as one condition is `True`, it executes that block and ignores the rest.

### Example

```python
score = 65

if score >= 70:
    print("Grade A")
elif score >= 60:
    print("Grade B")
else:
    print("Grade C")
```

Output:

```
Grade B
```

---

# Comparison Operators

| Operator | Meaning                  |
| -------- | ------------------------ |
| `==`     | Equal to                 |
| `!=`     | Not equal to             |
| `>`      | Greater than             |
| `<`      | Less than                |
| `>=`     | Greater than or equal to |
| `<=`     | Less than or equal to    |

These operators are used to compare values inside conditional statements.

---

# Logical Operators

Logical operators allow multiple conditions to be combined.

## `and`

Both conditions must be `True`.

```python
if age >= 18 and citizen:
    print("Eligible to vote")
```

---

## `or`

At least one condition must be `True`.

```python
if day == "Saturday" or day == "Sunday":
    print("Weekend")
```

---

## `not`

Reverses a condition.

```python
logged_in = False

if not logged_in:
    print("Please log in.")
```

---

# Nested `if`

A nested `if` is an `if` statement inside another `if` statement.

Example:

```python
age = 20

if age >= 18:
    if age >= 60:
        print("Senior Citizen")
    else:
        print("Adult")
```

---

# Common Beginner Mistakes

### Using `=` instead of `==`

Incorrect:

```python
if age = 18:
```

Correct:

```python
if age == 18:
```

* `=` assigns a value.
* `==` compares two values.

---

### Forgetting the Colon

Incorrect:

```python
if age >= 18
```

Correct:

```python
if age >= 18:
```

---

### Forgetting Indentation

Incorrect:

```python
if age >= 18:
print("Adult")
```

Correct:

```python
if age >= 18:
    print("Adult")
```

---

# Programs Built Today

* Age Checker
* Even or Odd Checker
* Password Checker
* Grade Calculator
* Student Result Checker

---

# Key Takeaways

* Conditional statements help programs make decisions.
* `if` executes code only when a condition is `True`.
* `if...else` is used when there are two possible outcomes.
* `if...elif...else` is used when there are multiple conditions.
* Python evaluates conditions from top to bottom.
* Proper indentation is required for conditional statements.
* `=` assigns values, while `==` compares values.
* Logical operators (`and`, `or`, `not`) make conditions more flexible.

---

# Summary

Today I learned how to make Python programs make decisions using conditional statements. I practiced using comparison operators, logical operators, nested `if` statements, and built several small projects, including a Student Result Checker that calculates grades and displays a formatted report based on user input.
