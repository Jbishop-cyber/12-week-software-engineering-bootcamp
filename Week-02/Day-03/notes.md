# Tuples & Dictionaries (Introduction)

## What is a Tuple?

A **tuple** is a collection of items, just like a list.

For example:

```python
students = ["Justice", "Ada", "John"]
```

is a **list**.

A tuple looks almost the same:

```python
students = ("Justice", "Ada", "John")
```

Notice the difference?

Lists use:

```python
[]
```

Tuples use:

```python
()
```

---

## Similarities

Both lists and tuples can:

* Store multiple values
* Store different data types
* Be indexed
* Be sliced
* Be looped through
* Be unpacked

Example:

```python
students = ("Justice", "Ada", "John")

print(students[0])
```

Output:

```text
Justice
```

Exactly like a list.

---

# The BIG Difference

A **list is mutable**.

That means it can change.

Example:

```python
students = ["Justice", "Ada", "John"]

students[1] = "Grace"

print(students)
```

Output:

```text
['Justice', 'Grace', 'John']
```

A **tuple is immutable**.

That means **once it's created, it cannot be changed**.

Example:

```python
students = ("Justice", "Ada", "John")

students[1] = "Grace"
```

Python says:

```text
TypeError: 'tuple' object does not support item assignment
```

because tuples cannot be modified.

---

## Why would anyone use tuples?

Imagine you're storing:

* Days of the week
* Months of the year
* RGB color values
* GPS coordinates
* A student's date of birth

Should these change accidentally?

Probably not.

Example:

```python
days = (
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
)
```

It makes sense that nobody should accidentally do:

```python
days[0] = "Christmas"
```

Tuples protect your data from accidental modification.

---

## Packing

Python automatically packs values into a tuple.

```python
student = "Justice", 24, "Python"
```

Python sees this as:

```python
student = ("Justice", 24, "Python")
```

---

## Unpacking

I have actually used tuple unpacking before!

Do you remember this?

```python
first, last = first_and_last(student_names)
```

That worked because my function returned:

```python
return first, last
```

which is actually returning a tuple:

```python
(first, last)
```

Another example:

```python
student = ("Justice", 90)

name, score = student

print(name)
print(score)
```

Output:

```text
Justice
90
```

| Feature      | List                     | Tuple |
| ------------ | ------------------------ | ----- |
| Syntax       | `[]`                     | `()`  |
| Can change?  | ✅ Yes                   | ❌ No  |
| Add items    | ✅ `append()`            | ❌ No  |
| Remove items | ✅ `remove()`, `pop()`   | ❌ No  |
| Indexing     | ✅ Yes                   | ✅ Yes |
| Looping      | ✅ Yes                   | ✅ Yes |
| Unpacking    | ✅ Yes                   | ✅ Yes |


## 🤔 When should I use a tuple?

Here's a simple rule that many Python developers follow:

a. If the data should never change, use a tuple.

b. If the data will change, use a list.

Examples:

### Use a List

Because students can be added or removed.

```python
students = ["Justice", "Ada", "John"]
```

### Use a Tuple

Because a person's date of birth shouldn't change.

```python
date_of_birth = (15, 8, 2002)
```

### Another Tuple Example

Coordinates on a map:

```python
location = (6.5244, 3.3792)
```

Latitude and longitude are fixed values, so a tuple makes sense.

## Does tuple have any methods like list?

> **Yes, but very few.**

## Why?

Remember:

> **Tuples are immutable.**

Since they **cannot be changed**, methods like these wouldn't make sense:

❌ `append()`
❌ `insert()`
❌ `remove()`
❌ `pop()`
❌ `sort()`
❌ `reverse()`
❌ `clear()`

Those methods all modify a list, which tuples are designed to prevent.

---

## Tuple Methods

Tuples only have **two built-in methods**.

## 1. `count()`

Counts how many times a value appears.

Example:

```python
numbers = (2, 5, 2, 8, 2)

print(numbers.count(2))
```

Output:

```text
3
```

Exactly the same behavior as `list.count()`.

---

## 2. `index()`

Returns the index of the first occurrence.

Example:

```python
names = ("Grace", "John", "Grace", "Ada")

print(names.index("Grace"))
```

Output:

```text
0
```

Just like the list version.

If the item isn't found:

```python
names.index("Justice")
```

raises:

```text
ValueError
```

---

## Functions That Also Work on Tuples

Even though tuples have only two methods, many **built-in functions** work with them.

### `len()`

```python
student = ("Justice", 90)

print(len(student))
```

Output:

```text
2
```

---

### `max()`

```python
numbers = (5, 8, 2, 10)

print(max(numbers))
```

Output:

```text
10
```

---

### `min()`

```python
numbers = (5, 8, 2, 10)

print(min(numbers))
```

Output:

```text
2
```

---

### `sum()`

```python
numbers = (5, 8, 2, 10)

print(sum(numbers))
```

Output:

```text
25
```

---

### `sorted()`

This one is interesting.

```python
numbers = (8, 2, 5, 1)

print(sorted(numbers))
```

Output:

```text
[1, 2, 5, 8]
```

Notice how `sorted()` returns a **list**, not a tuple, this is because tuples can't be modified.

---

## Quick Comparison

| Feature     | List | Tuple |
| ----------- | ---- | ----- |
| `append()`  | ✅    | ❌     |
| `insert()`  | ✅    | ❌     |
| `remove()`  | ✅    | ❌     |
| `pop()`     | ✅    | ❌     |
| `sort()`    | ✅    | ❌     |
| `reverse()` | ✅    | ❌     |
| `clear()`   | ✅    | ❌     |
| `count()`   | ✅    | ✅     |
| `index()`   | ✅    | ✅     |
| `len()`     | ✅    | ✅     |
| `max()`     | ✅    | ✅     |
| `min()`     | ✅    | ✅     |
| `sum()`     | ✅    | ✅     |

---

## A useful way to remember it

Think of it like this:

* **Lists** are like a notebook, we can add pages, erase things, and rearrange them.

* **Tuples** are like a printed certificate, once it's printed, you can read it and inspect it, but you don't change it.

That's why tuples only have methods for **looking at** their contents (`count()` and `index()`), not for **changing** them.

That's also why tuples are lightweight and often used for fixed collections of related values.

# 📘 Dictionaries

## Imagine this...

Suppose I ask you to store information about a student.

Using a list, you might do this:

```python
student = ["Justice", "Bishop", 90, "Python"]
```

Now imagine I ask you:

> **What is the student's score?**

You'd have to remember that the score is at index `2`:

```python
print(student[2])
```

🤔 That works, but it's not very readable. If someone else looked at your code, they wouldn't know what `student[2]` means without checking how the list was created.

---

## Dictionaries solve this problem.

A dictionary stores **key-value pairs**.

Think of it like a real dictionary:

| Word (Key) | Meaning (Value)       |
| ---------- | --------------------- |
| Apple      | A fruit               |
| Book       | A collection of pages |

In Python, it looks like this:

```python
student = {
    "first_name": "Justice",
    "last_name": "Bishop",
    "score": 90,
    "course": "Python"
}
```

Instead of using indexes, you use **keys**.

---

## Accessing Values

```python
print(student["first_name"])
```

Output:

```text
Justice
```

Another example:

```python
print(student["score"])
```

Output:

```text
90
```

Notice how much clearer that is than `student[2]`.

---

## Dictionary Syntax

```python
dictionary = {
    key1: value1,
    key2: value2,
    key3: value3
}
```

Keys are usually strings, although other immutable types (like integers or tuples) can also be used.

---

## json vs dictionaries:

Notice how a python dictionary looks similar to a json file?. However, they are **not the same thing**.

Let's compare them.

---

## Python Dictionary

```python
book = {
    "title": "Python Basics",
    "pages": 250,
    "author": "Justice"
}
```

This is a **Python object** that exists while your program is running.

You can do things like:

```python
book["price"] = 5000
del book["pages"]

print(book)
```

It can be modified, searched, looped through, and passed to functions.

---

## JSON

The same data in JSON looks like this:

```json
{
    "title": "Python Basics",
    "pages": 250,
    "author": "Justice"
}
```

It looks almost identical.

But JSON is **just a text format** for storing or exchanging data.

Think of JSON as a language that different programming languages can understand.

---

## An analogy

Imagine you have a contact saved in your phone.

Inside your Python program:

```python
person = {
    "name": "Justice",
    "age": 24
}
```

This is a **dictionary**.

When you save that information to a file or send it over the internet, it might become JSON:

```json
{
    "name": "Justice",
    "age": 24
}
```

When another program receives it, it converts the JSON back into its own data structure.

---

## The Main Differences

| Python Dictionary                            | JSON                           |
| -------------------------------------------- | ------------------------------ |
| Exists in Python memory                      | Text format                    |
| Can contain Python data types                | Only supports JSON data types  |
| Uses Python syntax                           | Uses JSON syntax               |
| Can call methods (`keys()`, `items()`, etc.) | Cannot; it's just text         |
| Used inside Python programs                  | Used to store or transfer data |

---

## One important difference

Python allows things that JSON does not.

For example:

```python
student = {
    "name": "Justice",
    "passed": True,
    "score": None
}
```

In Python:

* `True`
* `False`
* `None`

are valid values.

In JSON, they must be written as:

```json
{
    "name": "Justice",
    "passed": true,
    "score": null
}
```

Notice the differences:

* `True` → `true`
* `False` → `false`
* `None` → `null`

---

This matters because when we are dealing with 
* Flask
* APIs
* React
* .NET
* Databases

we'll constantly convert between Python dictionaries and JSON.

For example, a Flask API might return:

```python
return {
    "name": "Justice",
    "score": 90
}
```

and the client receives it as JSON:

```json
{
    "name": "Justice",
    "score": 90
}
```

## Note:

A dictionary is better than a list for storing student information because the data is organized using meaningful keys instead of index numbers. This makes the code easier to read, understand, and maintain.

## Rule of Thumb

Here's a rule you'll use throughout your programming career:

1. Use a list when you have a collection of similar items.

```python
students = ["Justice", "Ada", "John"]
```

2. Use a tuple when the data should not change.

```python
coordinates = (6.5244, 3.3792)
```

3. Use a dictionary when you want to describe something using named properties.

```python
student = {
    "name": "Justice",
    "score": 90,
    "course": "Python"
}
```

- A JSON object is essentially a dictionary.
- A database record often maps naturally to a dictionary.
- API responses are usually JSON, which becomes a dictionary in Python.
- Configuration files often represent settings as key-value pairs.

Awesome! 😄 Let's keep the momentum going.

---

# 📘 Dictionaries (Part 2)

## Adding New Items

Adding to a dictionary is surprisingly simple.

Suppose we have:

```python
student = {
    "name": "Justice",
    "score": 90
}
```

Now you want to store the student's grade.

Just assign a value to a **new key**:

```python
student["grade"] = "A"
```

Now the dictionary becomes:

```python
{
    "name": "Justice",
    "score": 90,
    "grade": "A"
}
```

Notice that `"grade"` didn't exist before. Python created it automatically.

---

## Updating Existing Values

Suppose Justice takes another test and scores **95**.

Simply assign a new value to the existing key:

```python
student["score"] = 95
```

Now:

```python
{
    "name": "Justice",
    "score": 95,
    "grade": "A"
}
```

Notice something interesting:

```python
student["score"] = 90
```

creates the key if it doesn't exist.

But if it **already exists**, it updates it.

Python automatically decides which one to do.

---

## Removing Items

There are several ways, but today we'll learn the simplest one.

Using `del`

```python
student = {
    "name": "Justice",
    "score": 90,
    "grade": "A"
}

del student["grade"]

print(student)
```

Output:

```python
{
    "name": "Justice",
    "score": 90
}
```

The `"grade"` key and its value are removed.

---

## What if the key doesn't exist?

```python
del student["age"]
```

Python raises a:

```text
KeyError
```

because `"age"` isn't in the dictionary.

It's similar to how:

```python
list.index()
```

raises a `ValueError` if the value isn't found.

---

## Looping Through a Dictionary

Suppose we have:

```python
student = {
    "name": "Justice",
    "score": 90,
    "grade": "A"
}
```

### Loop through the keys

```python
for key in student:
    print(key)
```

Output:

```text
name
score
grade
```

Notice:

By default, a `for` loop over a dictionary gives you the **keys**.

---

## Access the values

Since you have the key:

```python
for key in student:
    print(student[key])
```

Output:

```text
Justice
90
A
```

Python uses each key to retrieve its corresponding value.

---

### Get both key and value together

This is the most common pattern.

```python
for key, value in student.items():
    print(key, value)
```

Output:

```text
name Justice
score 90
grade A
```

This is called **dictionary unpacking**, just like tuple unpacking

```python
name, score = student_tuple
```

You're doing something similar here,`items()` gives you `(key, value)` pairs, and Python unpacks them into `key` and `value`.

---

## Other Useful Dictionary Methods

### `keys()`

Returns all the keys.

```python
student.keys()
```

---

### `values()`

Returns all the values.

```python
student.values()
```

---

### `items()`

Returns key-value pairs.

```python
student.items()
```

This is the method you'll use most often in loops.

---

# Quick Summary

| Operation        | Syntax                                    |
| ---------------- | ----------------------------------------- |
| Access value     | `student["score"]`                        |
| Add item         | `student["grade"] = "A"`                  |
| Update item      | `student["score"] = 95`                   |
| Delete item      | `del student["grade"]`                    |
| Loop keys        | `for key in student:`                     |
| Loop values      | `for key in student: print(student[key])` |
| Loop key & value | `for key, value in student.items():`      |

---

## One More Dictionary Method

## `get()`

Suppose you have:

```python
student = {
    "name": "Justice",
    "score": 90
}
```

If you do:

```python
print(student["grade"])
```

Python raises:

```text
KeyError: 'grade'
```

because `"grade"` doesn't exist.

But with `get()`:

```python
print(student.get("grade"))
```

Output:

```text
None
```

No error.

You can also provide a default value:

```python
print(student.get("grade", "Not Available"))
```

Output:

```text
Not Available
```

This is very useful when you're not sure whether a key exists.

---

## Difference between `[]` and `()`

## Square brackets `[ ]` — direct key access

```python
student["score"] = 95        # assignment
print(student["score"])      # retrieval
```

This is Python's built-in syntax for indexing — the same square-bracket syntax you already used with lists (`list[0]`). For dictionaries, it means "go directly to this key." It works for **both reading and writing**:

- On the left of `=` → it **sets** the value at that key (creates it if it doesn't exist, or overwrites if it does)

- On the right of `=` (or inside `print()`) → it **reads** the value at that key

But there's a catch: if the key *doesn't exist* and you try to **read** it this way, Python raises a `KeyError` and crashes:

```python
print(student["gpa"])   # KeyError: 'gpa' (if "gpa" was never set)
```

## Round brackets `( )` — calling a method

```python
student.get("score")
```

This isn't indexing at all — `.get(...)` is a **method** (a function that belongs to the dictionary object). Round brackets `()` are what Python always uses to **call a function or method** and pass it arguments — same as `print(...)` or `len(...)`.

`.get()` is a *safer* way to read a value because it won't crash if the key is missing — it just returns `None` (or a default you specify) instead:

```python
print(student.get("gpa"))          # None (no crash)
print(student.get("gpa", 0.0))     # 0.0 (your custom default)
```

## Why there's no `.get()` for assignment

`.get()` only exists for **reading** safely. There's no equivalent "safe assignment" method because assignment with `[ ]` never crashes — if the key doesn't exist yet, Python just creates it. So assignment only ever needs the one form: `student["score"] = 95`.

## Simple rule of thumb

| Bracket | What it means | Can it crash? |
|---|---|---|
| `dict["key"]` | direct access (read or write) | Yes, if reading a missing key |
| `dict.get("key")` | calling the `.get` method (read only) | No — returns `None` or default |


## Summary of the main dictionary methods

| Method      | Purpose                                            |
| ----------- | -------------------------------------------------- |
| `get(key)`  | Safely retrieve a value                            |
| `keys()`    | Return all keys                                    |
| `values()`  | Return all values                                  |
| `items()`   | Return all key-value pairs                         |
| `pop(key)`  | Remove a specific key and return its value         |
| `popitem()` | Remove and return the last inserted key-value pair |
| `update()`  | Update one or more key-value pairs                 |
| `clear()`   | Remove everything from the dictionary              |

---