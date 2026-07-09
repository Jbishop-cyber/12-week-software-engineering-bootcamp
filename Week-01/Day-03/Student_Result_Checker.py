# Student Result Checker

name = input("Enter your name: ")
score = int(input("Enter the score: "))
grade = ""
message = ""
width = 30
line = "=" * width
title = "STUDENT REPORT"
x = title.center(width)

if score >= 70:
    grade = "A"
    message = "Excellent work!"
elif score >= 60:
    grade = "B"
    message = "Very Good!"
elif score >= 50:
    grade = "C"
    message = "Good effort."
elif score >= 45:
    grade = "D"
    message = "Needs Improvement."
elif score >= 40:
    grade = "E"
    message = "Study Harder."
else:
    grade = "F"
    message = "Failed. Keep Practicing."

print(line)
print(x)
print(line)
print(f"Name: {name}")
print(f"Score: {score}")
print(f"Grade: {grade}")
print()
print(message)
print(line)
