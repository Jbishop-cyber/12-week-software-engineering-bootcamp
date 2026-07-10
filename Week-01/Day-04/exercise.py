# Exercise 1 — Count Up

def count_up():
    for i in range(1, 11):
        print(i)

count_up()

# Exercise 2 — Even Numbers

def print_even_numbers(n):
    if n < 2:
        print("No even numbers found.")
    else:
        for i in range(2, n+1, 2):
            print(i)

print_even_numbers(10)
print_even_numbers(1)

# Exercise 3 — Countdown

num = int(input("Enter a countdown number: "))

def countdown(n):
    if n < 1:
        print("Invalid Input")
    else:
        for i in range(n, 0, -1):
            print(i)
        print("Blast off!")

countdown(num)

# Exercise 4 Multiplication Table

num = int(input("Enter a number: "))

def multiplication_table(n):
    if n <= 0:
        print("Invalid number")
    else:
        for i in range(1, 11):
            print(f"{n} x {i} = {n * i}")

multiplication_table(num)

# Exercise 5 — Character Printer

text = input("Enter a text: ")

def print_characters(s):
    if s == "":
        print("Empty string")
    else:
        for character in s:
            print(character)

print_characters(text)