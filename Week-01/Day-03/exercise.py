# Exercise 1 — Age Checker

age = int(input("How old are you? "))

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")


# Exercise 2 — Even or Odd

number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")

# Exercise 3 — Password Checker

correct_password = "python123"
password = input("Enter your password: ")

if password == correct_password:
    print("Access Granted")
else:
    print("Access Denied")

# Exercise 4 — Grade Calculator

score = int(input("Enter your score: "))

if score >= 70:
    print("A")
elif score >= 60:
    print("B")
elif score >= 50:
    print("C")
elif score >= 45:
    print("D")
elif score >= 40:
    print("E")
else:
    print("F")
