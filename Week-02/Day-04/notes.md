# Week 2 – Day 4: Program Design

# 🤔 What is Program Design?

Program design is the process of **planning how a program should work before writing the code**.

Think of it like building a house.

You wouldn't start laying bricks before deciding:

* How many rooms?
* Where is the kitchen?
* Where is the bathroom?

You first create a **blueprint**.

Programming is the same.

Before coding, you create a **plan**.

---

## Why is Program Design Important?

Imagine someone tells you:

> "Build a Student Management System."

If you immediately start coding, you'll probably end up rewriting a lot of your work.

Instead, an experienced programmer asks:

* What should the program do?
* What information do I need?
* What functions will I need?
* What data structure should I use?

Only then do they begin coding.

---

# Example Problem

Suppose we want to build a calculator.

Many beginners think:

```text
I need to write Python code.
```

A programmer thinks:

```text
Step 1:
Ask for first number.

↓

Step 2:
Ask for second number.

↓

Step 3:
Ask which operation.

↓

Step 4:
Perform calculation.

↓

Step 5:
Display answer.
```

Notice...

**No Python yet.**

Just the plan.

---

# Algorithms

An **algorithm** is simply a sequence of steps to solve a problem.

For example:

### Problem

Find the largest number.

Algorithm:

```text
Start

↓

Assume first number is largest

↓

Compare every other number

↓

If a bigger number is found

↓

Replace largest

↓

Repeat until finished

↓

Print largest

↓

End
```

That's an algorithm.

---

# Pseudocode

Pseudocode is writing the algorithm in plain English that looks a little like code.

Example:

```text
BEGIN

Ask user for age

IF age >= 18
    Print "Adult"
ELSE
    Print "Minor"

END
```

Notice:

* Not Python
* Not English paragraphs

It's somewhere in between.

---

# Flowcharts

A flowchart is a **diagram** of the program.

Example:

```text
        Start
          │
          ▼
 Ask for age
          │
          ▼
   Is age ≥ 18?
      /       \
    Yes        No
     │          │
     ▼          ▼
 Print Adult  Print Minor
      \        /
       ▼      ▼
         End
```

Flowcharts help you visualize the program before writing code.

---

# Breaking Problems into Functions

Remember your Inventory Manager?

Instead of one huge function, you wrote:

```python
get_number_of_products()

store_products()

display_inventory()

search_product()

update_quantity()
```

That **is** program design.

You broke one large problem into smaller, manageable pieces.

---

# Choosing the Right Data Structure

A good programmer asks:

> "What is the best way to store this data?"

Examples:

| Problem            | Best Structure |
| ------------------ | -------------- |
| Student names      | List           |
| Coordinates (x, y) | Tuple          |
| Student record     | Dictionary     |
| Inventory          | Dictionary     |

Choosing the right data structure makes the rest of the program much easier.

---

# Real Example

Imagine you're asked to build a library system.

Instead of coding immediately, you'd think:

```text
What does the program need?

✔ Add books

✔ Remove books

✔ Search books

✔ Borrow books

✔ Return books
```

Then turn those into functions:

```python
add_book()

remove_book()

search_book()

borrow_book()

return_book()
```

Only after that do you start writing Python.

---

# The Four Steps I Want You to Follow

From today onward, before writing any program, ask yourself these four questions:

### 1️⃣ What is the problem?

Example:

> Store student records.

---

### 2️⃣ What data do I need?

Example:

* Name
* Score
* Grade

---

### 3️⃣ What functions do I need?

Example:

```text
add_student()

search_student()

display_students()
```

---

### 4️⃣ What data structure should I use?

Example:

```text
Dictionary
```
---

# Part 2 – Program Design Patterns

There are a few patterns you'll start seeing in almost every program you write.

### 1. Input → Process → Output (IPO)

Every program follows this basic structure.

Example: Average Score Calculator

```
Input
│
├── Enter student names
├── Enter scores
│
▼
Process
│
├── Calculate total
├── Calculate average
├── Find highest score
│
▼
Output
│
├── Display report
```

Think about your Inventory Manager:

**Input**

* Product names
* Quantities

↓

**Process**

* Store products
* Search products
* Update quantities

↓

**Output**

* Display inventory

Without realizing it, you've already been following the IPO model.

---

## 2. Top-Down Design

This is one of the most useful design techniques.

Instead of solving every detail at once, start with the big picture.

Example:

```
Student Management System

↓

Get student information

↓

Store information

↓

Search information

↓

Update information

↓

Display report
```

Then break each step down again.

For example:

```
Store information

↓

Ask for name

↓

Ask for score

↓

Save in dictionary
```

This is exactly how large software is built.

---

## 3. Modular Programming

Instead of writing one giant program:

```python
# 300 lines here...
```

Break it into small pieces.

```
main()

↓

add_student()

↓

search_student()

↓

display_students()

↓

update_student()
```

This makes programs much easier to understand and maintain.

---

# Part 3 – Design Exercise (Before Coding)

Imagine someone asks you to build a **Library Management System**.

The features are:

* Add a book
* Borrow a book
* Return a book
* Search for a book
* Display all books
* Exit

Don't write Python.

Design it.

Draw something like this:

```
Library System

↓

What data structure?

↓

What functions?

↓

Algorithm

↓

Validation
```