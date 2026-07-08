# Week 1 - Day 2 Notes

## User Input

The `input()` function allows a program to receive information from the user while it is running.

Example:

```python
name = input("Enter your name: ")
```

The program pauses and waits until the user enters a value.

---

## Important Rule

**The `input()` function always returns a string (`str`).**

Example:

```python
age = input("Enter your age: ")

print(type(age))
```

Output:

```
<class 'str'>
```

Even if the user types `24`, Python stores it as `"24"`.

---

## Type Conversion (Casting)

Type conversion changes one data type into another.

### Convert to Integer

```python
age = int(input("Enter your age: "))
```

### Convert to Float

```python
height = float(input("Enter your height: "))
```

### Convert to String

```python
number = 100
text = str(number)
```

---

## Why Type Conversion Matters

Without conversion:

```python
age = input("Age: ")
print(age + age)
```

If the user enters:

```
30
```

Output:

```
3030
```

Python joins two strings together.

With conversion:

```python
age = int(input("Age: "))
print(age + age)
```

Output:

```
60
```

Now Python performs mathematical addition.

---

## F-Strings

F-strings make it easier to insert variables into text.

Example:

```python
name = "Jay"
age = 24

print(f"My name is {name} and I am {age} years old.")
```

Output:

```
My name is Jay and I am 24 years old.
```

---

## Arithmetic Operators Reviewed

| Operator | Meaning             | Example       |
| -------- | ------------------- | ------------- |
| `+`      | Addition            | `5 + 3 = 8`   |
| `-`      | Subtraction         | `5 - 3 = 2`   |
| `*`      | Multiplication      | `5 * 3 = 15`  |
| `/`      | Division            | `5 / 2 = 2.5` |
| `//`     | Floor Division      | `5 // 2 = 2`  |
| `%`      | Modulus (Remainder) | `5 % 2 = 1`   |

---

## Best Practices Learned

* Use meaningful variable names.
* Use `snake_case` for variable names.
* Convert user input before performing calculations.
* Prefer f-strings over string concatenation for readability.
* Keep code properly indented and easy to read.

---

## Common Mistakes

❌ Forgetting to convert user input before doing calculations.

```python
age = input("Age: ")
print(age + 5)
```

This causes a `TypeError`.

✅ Correct:

```python
age = int(input("Age: "))
print(age + 5)
```

---

## Summary

Today I learned how to create interactive Python programs by accepting user input, converting data types when necessary, performing calculations, and displaying clean, formatted output using f-strings. These concepts are essential for building applications that respond to user input.
