# 📚 Lists

## Why Do We Need Lists?

Imagine you want to store the names of five students.

Without lists:

```python
student1 = "Justice"
student2 = "Ada"
student3 = "John"
student4 = "Grace"
student5 = "David"
````

This quickly becomes difficult to manage.

A list allows us to store multiple values in a single variable. Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

Lists are created using square brackets

```python
students = ["Justice", "Ada", "John", "Grace", "David"]
```

Lists make programs shorter, cleaner, and easier to maintain.

---

## Creating a List

Lists are created using square brackets `[]`.

```python
numbers = [10, 20, 30, 40]
names = ["Justice", "Ada", "John"]
mixed = ["Python", 3, True]
```

An empty list:

```python
students = []
```

---

## Accessing List Elements

Each item in a list has an index.

```python
students = ["Justice", "Ada", "John"]
```

| Index | Value   |
| ----- | ------- |
| 0     | Justice |
| 1     | Ada     |
| 2     | John    |

Examples:

```python
print(students[0])
```

Output:

```
Justice
```

```python
print(students[2])
```

Output:

```
John
```

---

## Negative Indexing

Negative indexes count from the end.

```python
students = ["Justice", "Ada", "John"]
```

| Index | Value   |
| ----- | ------- |
| -1    | John    |
| -2    | Ada     |
| -3    | Justice |

Example:

```python
print(students[-1])
```

Output:

```
John
```

---

## Adding Items

Use `append()` to add an item to the end of a list.

```python
students = []

students.append("Justice")
students.append("Ada")
```

Result:

```python
["Justice", "Ada"]
```

---

## Updating Items

Lists are mutable, meaning their values can be changed.

```python
students = ["Justice", "Ada", "John"]

students[1] = "Grace"
```

Result:

```python
["Justice", "Grace", "John"]
```

---

## Getting the Length of a List

Use `len()` to count the number of items.

```python
students = ["Justice", "Ada", "John"]

print(len(students))
```

Output:

```
3
```

---

## Looping Through a List

Using a `for` loop:

```python
students = ["Justice", "Ada", "John"]

for student in students:
    print(student)
```

Output:

```
Justice
Ada
John
```

---

## Returning Multiple Values

Python functions can return more than one value.

Example:

```python
def first_last(numbers):
    first = numbers[0]
    last = numbers[-1]

    return first, last
```

Usage:

```python
first, last = first_last([10, 20, 30, 40])

print(first)
print(last)
```

Output:

```
10
40
```

Python returns multiple values as a tuple.

---

## Common List Functions

### Maximum Value

```python
scores = [70, 85, 92]

print(max(scores))
```

Output:

```
92
```

### Minimum Value

```python
print(min(scores))
```

Output:

```
70
```

### Sum

```python
print(sum(scores))
```

Output:

```
247
```

---

## Common Beginner Mistakes

### ❌ Using parentheses instead of square brackets

Wrong:

```python
students = ("Justice", "Ada")
```

Correct:

```python
students = ["Justice", "Ada"]
```

---

### ❌ Accessing an index that doesn't exist

Wrong:

```python
students = ["Justice", "Ada"]

print(students[5])
```

Result:

```
IndexError
```

---

### ❌ Forgetting to append new items

Wrong:

```python
students = []

name = input("Name: ")
```

Nothing is stored.

Correct:

```python
students.append(name)
```

---

### ❌ Confusing tuples with lists

```python
return first, last
```

returns a **tuple**.

```python
return [first, last]
```

returns a **list**.

Remember:

* `()` → Tuple
* `[]` → List

`````