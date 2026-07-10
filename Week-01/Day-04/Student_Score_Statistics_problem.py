student_name = []
student_score = []

width = 26
line = "=" * width
title = "CLASS REPORT"
middle = title.center(width)

num_students = int(input("How many students? "))

while num_students <= 0:
    print("Invalid number of students")
    num_students = int(input("How many students? "))

for i in range(num_students):
    name, score = input("Enter student name and score (e.g. Jay 90): ").split()
    score = int(score)
        
    while score < 0 or score > 100:
        print("Invalid score")
        score = int(input("Enter student score: "))
	
    student_name.append(name)
    student_score.append(score)

average = sum(student_score) / num_students

print(line)
print(title)
print(line)
print(f"Total Students: {num_students}")
print(f"Highest Score: {max(student_score)}")
print(f"Lowest Score: {min(student_score)}")
print(f"Average Score: {average:.2f}")
print(line)