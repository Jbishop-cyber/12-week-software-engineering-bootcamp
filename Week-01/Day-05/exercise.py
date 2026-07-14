# Exercise 1 — Maximum Number

def maximum_number(a, b):
    if a > b:
        return a
    elif b > a:
        return b
    else:
        return a

print(maximum_number(7, 15))


# Exercise 2 — Is Even

def is_even(n):
    if n % 2 == 0:
        return True
    elif n % 2 != 0:
        return False
print(is_even(8))
print(is_even(5))

# Exercise 3 — Grade Calculator

def calculate_grade(n):
    grade = ""
    if n < 0 or n > 100:
        return "Invalid score"
    elif n >= 70:
        grade = "A"
    elif n >= 60:
        grade = "B"
    elif n >= 50:
        grade = "C"
    elif n >= 45:
        grade = "D"
    elif n >= 40:
        grade = "E"
    else:
        grade = "F"
    return grade

print(calculate_grade(82))
print(calculate_grade(35))
print(calculate_grade(150))

# Exercise 4 — Count Vowels

def count_vowels(n):
    vowels = "aeiouAEIOU"
    count = 0
    for character in n:
        if character in vowels:
            count += 1
    return count

print(count_vowels("Programming"))


# Exercise 5 — Factorial

def factorial(n):
    if n < 0:
        return -1
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(7))

# Exercise 6 - Digit Len:

def digit_length(n):
    if n < 0:
        return -1
    if n < 10:
        return 1
    else:
        return 1 + digit_length(n // 10)

print(digit_length(12345678910))
