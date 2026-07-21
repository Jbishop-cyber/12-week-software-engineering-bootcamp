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

## List Methods

List methods are built-in functions that belong to Python lists. They allow us to add, remove, search, sort, and modify items in a list.

Methods are called using **dot notation**:

```python
students.append("Justice")
```

where:

* `students` is the list.
* `append()` is the method.

---

## 1. `append()`

Adds an item to the **end** of a list.

### Syntax

```python
list.append(item)
```

### Example

```python
students = ["Ada", "John"]

students.append("Justice")

print(students)
```

Output:

```python
['Ada', 'John', 'Justice']
```

### Use Case

* Adding new records.
* Collecting user input.
* Building a list inside a loop.

---

## 2. `insert()`

Adds an item at a specific index.

### Syntax

```python
list.insert(index, item)
```

### Example

```python
students = ["Ada", "John"]

students.insert(1, "Justice")
```

Output

```python
['Ada', 'Justice', 'John']
```

### Use Case

When the position of the new item matters.

---

## 3. `remove()`

Removes the **first occurrence** of a value.

### Syntax

```python
list.remove(value)
```

Example

```python
numbers = [2, 4, 6, 4]

numbers.remove(4)
```

Output

```python
[2, 6, 4]
```

Notice only the first `4` was removed.

### Beginner Mistake

If the value doesn't exist,

```python
numbers.remove(10)
```

Python raises a `ValueError`.

---

#$ 4. `pop()`

Removes an item by its index.

### Syntax

```python
list.pop(index)
```

Example

```python
students = ["Ada", "John", "Justice"]

removed = students.pop(1)
```

Output

```python
removed = "John"

students = ["Ada", "Justice"]
```

### Important

Unlike `remove()`, `pop()` returns the removed item.

---

## 5. `index()`

Returns the index of the **first occurrence** of a value.

### Syntax

```python
list.index(value)
```

Example

```python
students = ["Ada", "John", "Justice"]

print(students.index("John"))
```

Output

```python
1
```

### Important

If the value doesn't exist,

```python
students.index("Grace")
```

raises a `ValueError`.

---

## 6. `count()`

Counts how many times a value appears.

### Syntax

```python
list.count(value)
```

Example

```python
numbers = [2, 5, 2, 8, 2]

print(numbers.count(2))
```

Output

```python
3
```

### Use Case

Finding duplicates.

---

## 7. `sort()`

Sorts the original list.

### Syntax

```python
list.sort()
```

Example

```python
numbers = [8, 2, 5, 1]

numbers.sort()
```

Output

```python
[1, 2, 5, 8]
```

Descending order

```python
numbers.sort(reverse=True)
```

Output

```python
[8, 5, 2, 1]
```

---

## 8. `reverse()`

Reverses the current order.

### Syntax

```python
list.reverse()
```

Example

```python
numbers = [1, 2, 3]

numbers.reverse()
```

Output

```python
[3, 2, 1]
```

### Difference from `sort(reverse=True)`

```python
numbers.reverse()
```

simply flips the list.

```python
numbers.sort(reverse=True)
```

sorts the list from largest to smallest.

---

## 9. `clear()`

Removes every item from the list.

### Syntax

```python
list.clear()
```

Example

```python
students = ["Ada", "John"]

students.clear()
```

Output

```python
[]
```

The list still exists, but it contains no items.

---

## Summary Table

| Method      | Purpose                               |
| ----------- | ------------------------------------- |
| `append()`  | Add item to the end                   |
| `insert()`  | Add item at a specific index          |
| `remove()`  | Remove the first matching value       |
| `pop()`     | Remove an item by index and return it |
| `index()`   | Find the index of a value             |
| `count()`   | Count occurrences of a value          |
| `sort()`    | Sort the list                         |
| `reverse()` | Reverse the current order             |
| `clear()`   | Remove all items                      |

---

## Things to Remember

* Methods belong to objects and are called using dot notation.
* `append()` always adds to the end.
* `insert()` adds at a chosen position.
* `remove()` removes by value.
* `pop()` removes by index.
* `index()` finds the first occurrence.
* `count()` counts occurrences.
* `sort()` changes the order permanently.
* `reverse()` flips the list without sorting it.
* `clear()` empties the list.

---

## Key Concepts Learned

* Lists
* Searching
* List methods 
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