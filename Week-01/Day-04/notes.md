# 🔁 Loops

## Why Do We Need Loops?

Imagine you want to print:

```python
print("Hello, Jay!")
```

five times.

Without loops:

```python
print("Hello, Jay!")
print("Hello, Jay!")
print("Hello, Jay!")
print("Hello, Jay!")
print("Hello, Jay!")
```

It works...

But imagine printing it **1,000 times**. That would be repetitive and inefficient.

A loop allows the computer to repeat a task automatically.

Python has two main types of loops:

- `while`
- `for`

---

# The `while` Loop

A `while` loop repeats as long as a condition remains `True`.

## Syntax

```python
while condition:
    # code
```

## Example

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

Output:

```
1
2
3
4
5
```

### Why is `count += 1` important?

```python
count += 1
```

updates the value of `count` after every iteration.

Without it:

```python
count = 1

while count <= 5:
    print(count)
```

The condition is always `True`, causing the program to run forever.

This is called an **infinite loop**.

---

# The `for` Loop

A `for` loop is used when you know how many times something should repeat or when looping through a sequence.

Example:

```python
for number in range(5):
    print(number)
```

Output:

```
0
1
2
3
4
```

### Why does it start at 0?

Because:

```python
range(5)
```

produces:

```
0
1
2
3
4
```

Python stops **before** the ending value.

---

# The `range()` Function

There are three common ways to use `range()`.

## 1. One Argument

```python
range(5)
```

Produces:

```
0
1
2
3
4
```

---

## 2. Two Arguments

```python
range(1, 6)
```

Produces:

```
1
2
3
4
5
```

The first value is included.

The second value is **not**.

---

## 3. Three Arguments

```python
range(start, stop, step)
```

Example:

```python
for number in range(2, 11, 2):
    print(number)
```

Output:

```
2
4
6
8
10
```

The third argument (`step`) determines how much the value increases (or decreases) after each iteration.

---

# Looping Through a String

Strings are sequences of characters.

```python
name = "Jay"

for letter in name:
    print(letter)
```

Output:

```
J
a
y
```

---

# `break`

`break` immediately terminates the loop.

Example:

```python
for number in range(1, 11):
    if number == 6:
        break
    print(number)
```

Output:

```
1
2
3
4
5
```

---

# `continue`

`continue` skips the current iteration and moves to the next one.

```python
for number in range(1, 6):
    if number == 3:
        continue
    print(number)
```

Output:

```
1
2
4
5
```

Notice that `3` is skipped.

---

# Nested Loops

A nested loop is simply **a loop inside another loop**.

```python
for row in range(3):
    for column in range(4):
        print("*", end=" ")
    print()
```

Output:

```
* * * *
* * * *
* * * *
```

The outer loop controls the rows.

The inner loop controls the columns.

For **every iteration of the outer loop**, the inner loop runs from beginning to end.

---

# Choosing Between `for` and `while`

Use a **for loop** when:

- You know how many times something should repeat.
- You're looping through a sequence (list, string, range, etc.).

Use a **while loop** when:

- You don't know how many times the loop will run.
- The loop depends on a condition becoming `False`.
- You're validating user input.

---

# Common Beginner Mistakes

## ❌ Forgetting to update the loop variable

```python
count = 1

while count <= 5:
    print(count)
```

Infinite loop.

Correct:

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

---

## ❌ Wrong indentation

Wrong:

```python
for i in range(5):
print(i)
```

Correct:

```python
for i in range(5):
    print(i)
```

---

## ❌ Expecting `range(5)` to include 5

Remember:

```python
range(5)
```

means:

```
0
1
2
3
4
```

---

## ❌ Using a `for` loop for input validation

Instead of:

```python
for i in range(5):
    score = int(input("Enter score: "))
```

Use a `while` loop:

```python
score = int(input("Enter score: "))

while score < 0 or score > 100:
    print("Invalid score")
    score = int(input("Enter score: "))
```

This keeps asking until the user enters a valid value.