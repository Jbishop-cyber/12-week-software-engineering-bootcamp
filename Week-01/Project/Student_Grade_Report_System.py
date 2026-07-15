# STUDENT GRADE REPORT SYSTEM

def get_number_of_students():
    num_students = int(input("Enter the total number of students: "))

    while num_students <= 0:
        print("Invalid number of students")
        num_students = int(input("Enter the total number of students: "))
    return num_students

def calculate_grade(score):
    grade = ""
    if score >= 70:
        grade = "A"
    elif score >= 60:
        grade = "B"
    elif score >= 50:
        grade = "C"
    elif score >= 40:
        grade = "D"
    else:
        grade = "F"
    return grade

def calculate_remark(grade):
    remark = ""
    if grade == "A":
        remark = "Excellent work!"
    elif grade == "B":
        remark = "Very Good!"
    elif grade == "C":
        remark = "Good effort."
    elif grade == "D":
        remark = "Needs Improvement."
    else:
        remark = "Failed. Keep Practicing."
    return remark

def calculate_average(student_scores):
    return sum(student_scores) / len(student_scores)

def display_student_report(name, surname, score, grade, remark):
    width = 30
    line = "=" * width
    title = "STUDENT REPORT"
    middle = title.center(width)

    print(line)
    print(middle)
    print(line)
    print(f"Name: {name}")
    print(f"Surname: {surname}")
    print(f"Score: {score}")
    print(f"Grade: {grade}")
    print()
    print(remark)
    print(line)

def display_class_summary(num_students, calculate_average, student_scores):
    width = 30
    line = "=" * width
    title = "CLASS SUMMARY"
    middle = title.center(width)

    print(line)
    print(middle)
    print(line)
    print(f"Total Students: {num_students}")
    print(f"Average Score: {calculate_average:.2f}")
    print(f"Highest Score: {max(student_scores)}")
    print(f"Lowest Score: {min(student_scores)}")
    print(line)

num_students = get_number_of_students()
student_scores = []

for i in range(num_students):
    name, surname, score = input("Enter student name, surname and score (e.g. Justice Bishop 90): ").split()
    score = int(score)

    while score < 0 or score > 100:
        print("Invalid score")
        score = int(input("Enter student score: "))
        
    grade = calculate_grade(score)
    remark = calculate_remark(grade)
    display_student_report(name, surname, score, grade, remark)
    
    student_scores.append(score)

display_class_summary(num_students, calculate_average(student_scores), student_scores)