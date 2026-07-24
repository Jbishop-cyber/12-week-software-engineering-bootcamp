# Nested Dictionaries

## What is a Nested Dictionary?

A **nested dictionary** is simply:

> **A dictionary that contains another dictionary as its value.**

You've already worked with a normal dictionary.

```python
student = {
    "name": "Justice",
    "score": 95,
    "grade": "A"
}
```

Think of it like a form with three fields.

---

Now imagine you have **three students**.

A normal dictionary isn't enough because each student has multiple pieces of information.

So instead, each student becomes **its own dictionary**.

```python
students = {
    "Justice": {
        "score": 95,
        "grade": "A"
    },

    "Grace": {
        "score": 88,
        "grade": "B"
    },

    "Victor": {
        "score": 76,
        "grade": "C"
    }
}
```

Notice the structure.

The **outer dictionary** stores students.

Each **value** is another dictionary.

```
students
│
├── Justice
│      ├── score : 95
│      └── grade : A
│
├── Grace
│      ├── score : 88
│      └── grade : B
│
└── Victor
       ├── score : 76
       └── grade : C
```

This is why it's called **nested**.

---

## Accessing Values

Suppose you want Justice's score.

Think of it in two steps.

Step 1:

Find Justice.

```python
students["Justice"]
```

This returns

```python
{
    "score":95,
    "grade":"A"
}
```

Now find the score.

```python
students["Justice"]["score"]
```

Output

```python
95
```

---

Justice's grade:

```python
print(students["Justice"]["grade"])
```

Output

```
A
```

---

## Changing Values

Suppose Justice scored 100.

```python
students["Justice"]["score"] = 100
```

Now the dictionary becomes

```python
"Justice": {
    "score":100,
    "grade":"A"
}
```

---

## Adding More Information

Suppose later you want to add a course.

```python
students["Justice"]["course"] = "Python"
```

Now Justice becomes

```python
"Justice": {
    "score":100,
    "grade":"A",
    "course":"Python"
}
```

You didn't recreate the dictionary.

You simply added another key.

---

## Adding Another Student

Suppose a new student joins.

```python
students["John"] = {
    "score":82,
    "grade":"B"
}
```

Now John has been added.

---

## Removing a Student

```python
students.pop("Grace")
```

Grace is gone.

---

## Checking if a Student Exists

```python
if "Justice" in students:
    print("Student exists")
```

This is much faster than looping through a list.

---

## Looping Through a Nested Dictionary

Suppose you want to print everyone's information.

```python
for name, details in students.items():
    print(name)
    print(details)
```

Output

```
Justice
{'score':95,'grade':'A'}

Grace
{'score':88,'grade':'B'}
```

---

But we can go even further.

```python
for name, details in students.items():
    print(f"Name: {name}")

    for key, value in details.items():
        print(f"{key}: {value}")

    print()
```

Output

```
Name: Justice
score: 95
grade: A

Name: Grace
score: 88
grade: B
```

Notice there are **two loops**:

* The outer loop goes through each student.
* The inner loop goes through each student's details.

---

## Why Nested Dictionaries?

Imagine using a list instead.

```python
students = [
    ["Justice",95,"A"],
    ["Grace",88,"B"]
]
```

Now imagine six months later.

What is

```python
student[1]
```

Score?

Age?

Course?

You have to remember.

With dictionaries, it's obvious.

```python
student["score"]
```

Much easier to read.

---

## Real-World Examples

A library system

```python
books = {
    "Harry Potter": {
        "genre":"Fantasy",
        "author":"J.K Rowling",
        "available":True
    }
}
```

A bank

```python
accounts = {
    "12345678": {
        "name":"Justice",
        "balance":5000,
        "pin":1234
    }
}
```

An inventory

```python
inventory = {
    "Rice": {
        "quantity":25,
        "price":45000
    }
}
```

A game

```python
players = {
    "Player1": {
        "health":100,
        "level":8,
        "coins":320
    }
}
```