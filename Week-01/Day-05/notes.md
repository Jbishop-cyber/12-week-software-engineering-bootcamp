# 🧩 Functions

## Why Do We Need Functions?

Imagine you need to calculate the average score of students in several different parts of your program.

Without functions, you might write the same code over and over again.

```python
average = sum(scores) / len(scores)
print(average)

average = sum(scores2) / len(scores2)
print(average)
````

This makes your code repetitive, harder to read, and more difficult to maintain.

Functions solve this problem by allowing you to write a block of code once and reuse it whenever you need it.

A function is a reusable block of code that performs a specific task.

---

## Defining a Function

A function is defined using the `def` keyword.

### Syntax

```python
def function_name():
    # code
```

Example:

```python
def greet():
    print("Hello, Jay!")
```

Nothing happens when a function is defined.

To execute it, you must call it.

```python
greet()
```

Output:

```
Hello, Jay!
```

---

## Function Parameters

A parameter is a variable listed inside the parentheses when defining a function.

Example:

```python
def greet(name):
    print(f"Hello, {name}!")
```

Here, `name` is the parameter.

---

## Function Arguments

An argument is the actual value passed to the function.

Example:

```python
greet("Jay")
```

Output:

```
Hello, Jay!
```

In this example:

* Parameter → `name`
* Argument → `"Jay"`

---

## Functions Without Parameters

Some functions do not need any information.

Example:

```python
def welcome():
    print("Welcome!")
```

Call it with:

```python
welcome()
```

---

## Functions With Multiple Parameters

A function can accept more than one parameter.

Example:

```python
def add(a, b):
    print(a + b)
```

Calling:

```python
add(5, 3)
```

Output:

```
8
```

---

## The `return` Statement

A function can return a value back to the part of the program that called it.

Example:

```python
def add(a, b):
    return a + b
```

Using it:

```python
result = add(5, 3)
print(result)
```

Output:

```
8
```

Unlike `print()`, `return` sends the value back to the caller.

---

## `print()` vs `return`

These are not the same.

### Using `print()`

```python
def greet():
    print("Hello")
```

Calling:

```python
greet()
```

Output:

```
Hello
```

The function displays the text but does not return a value.

---

### Using `return`

```python
def greet():
    return "Hello"
```

Calling:

```python
print(greet())
```

Output:

```
Hello
```

The function returns the value, and `print()` displays it.

---

## Why Does `print(function())` Display `None`?

Example:

```python
def greet():
    print("Hello")

print(greet())
```

Output:

```
Hello
None
```

Explanation:

The function prints `"Hello"`.

Since there is no `return` statement, Python automatically returns `None`.

Then the outer `print()` prints that returned value.

---

## Returning Multiple Values

Python allows a function to return more than one value.

Example:

```python
def student():
    return "Jay", 90
```

Receiving the values:

```python
name, score = student()
```

Now:

```python
print(name)
print(score)
```

Output:

```
Jay
90
```

This is called **tuple unpacking**.

---

## Local Variables

Variables created inside a function exist only inside that function.

Example:

```python
def test():
    number = 10
    print(number)
```

Trying to use `number` outside the function causes an error because it is local to the function.

---

## Why We Pass Arguments

Instead of using global variables, pass the information a function needs.

Bad example:

```python
score = 80

def show():
    print(score)
```

Better:

```python
def show(score):
    print(score)

show(80)
```

This makes functions more reusable and easier to understand.

---

## Breaking Programs Into Functions

Large programs should be divided into smaller functions.

Instead of writing everything in one block:

```python
# Very long program...
```

Use functions:

```python
get_number_of_students()
get_student_scores()
calculate_average()
display_report()
```

This makes programs easier to read, test, and maintain.

---

# Common Beginner Mistakes

## ❌ Forgetting to Call the Function

Wrong:

```python
def greet():
    print("Hello")
```

Nothing happens.

Correct:

```python
greet()
```

---

## ❌ Forgetting `return`

Wrong:

```python
def add(a, b):
    a + b
```

Correct:

```python
def add(a, b):
    return a + b
```

---

## ❌ Confusing `print()` and `return`

Wrong:

```python
def square(n):
    print(n * n)
```

if the question asks you to **return** the answer.

Correct:

```python
def square(n):
    return n * n
```

---

## ❌ Using Global Variables Unnecessarily

Instead of:

```python
total = 0

def calculate():
    print(total)
```

Pass the value:

```python
def calculate(total):
    print(total)
```

---

# Key Takeaways

* A function is a reusable block of code.
* Functions are defined using the `def` keyword.
* Parameters receive information.
* Arguments provide information.
* `print()` displays output.
* `return` sends a value back to the caller.
* A function can return multiple values.
* Variables created inside a function are local.
* Passing arguments makes functions cleaner and more reusable.
* Breaking large programs into smaller functions makes code easier to read, maintain, and debug.
