"""Exercise 1:

Write a program that asks for:

Name
Age
Country

Then display:

Welcome, Jay!
You are 24 years old.
You live in Nigeria.
"""

name = input("What is your name? ")
age = input("How old are you? ")
country = input("What country are you from? ")

print(f"Welcome, {name}!")
print(f"You are {age} years old.")
print(f"You live in {country}.")


"""Exercise 2

Ask the user for two numbers.

Print:

Sum
Difference
Product
Quotient

Example:

First number: 10
Second number: 2

Sum: 12
Difference: 8
Product: 20
Quotient: 5.0
"""

first_number = int(input("Enter the first number: "))
second_number = int(input("Enter second number: "))

print(f"Sum: {first_number + second_number}")
print(f"Difference: {first_number - second_number}")
print(f"Product: {first_number * second_number}")
print(f"Quotient: {first_number / second_number}")


"""Exercise 3

Ask the user:

What is your birth year?

Assume the current year is 2026.

Calculate and print their age.

Example:

Birth year: 2002

You are 24 years old.
"""

birth_year = int(input("What is your birth year? "))

age = 2026 - birth_year

print(f"Birth year: {birth_year}")
print(f"You are {age} years old.")
