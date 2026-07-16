def get_number_of_students():
    num_students = int(input("Enter the total number of students: "))

    while num_students <= 0:
        print("Please enter a vaild number!")
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
    elif score >= 45:
        grade = "D"
    elif score >= 40:
        grade = "E"
    else:
        grade = "F"
    return grade

def calculate_remark(grade):
    remark = ""

    if grade == "A":
        remark = "Excellent!"
    elif grade == "B":
        remark = "Very Good!"
    elif grade == "C":
        remark = "Good!"
    elif grade == "D":
        remark = "Average!"
    elif grade == "E":
        remark = "Below Average!"
    else:
        remark = "Fail!"
    return remark

def display_student_report(name, surname, score, grade, remark):
    width = 30
    line = "=" * width
    title = "STUDENT REPORT"
    middle = title.center(width)

    print(line)
    print(middle)
    print(line)
    print(f"NAME: {name}")
    print(f"SURNAME: {surname}")
    print(f"SCORE: {score}")
    print(f"GRADE: {grade}")
    print()
    print(f"{remark}")
    print(line)

def calculate_average(student_scores, num_students):
    average = sum(student_scores) / num_students
    return average

def calculate_class_grade(average):
    class_grade = ""

    if average >= 70:
        class_grade = "A"
    elif average >= 60:
        class_grade = "B"
    elif average >= 50:
        class_grade = "C"
    elif average >= 45:
        class_grade = "D"
    elif average >= 40:
        class_grade = "E"
    else:
        class_grade = "F"
    return class_grade

def calculate_class_remark(class_grade):
    class_remark = ""

    if class_grade == "A":
        class_remark = "EXCELLENT JOB!"
    elif class_grade == "B":
        class_remark = "WELL DONE!"
    elif class_grade == "C":
        class_remark = "NOT BAD!"
    elif class_grade == "D":
        class_remark = "NEEDS IMPROVEMENT!"
    elif class_grade == "E":
        class_remark = "POOR!"
    else:
        class_remark = "OMO UNA NOR TRY OH!"
    return class_remark

def display_class_summary(num_students, student_scores, calculate_average, class_grade, class_remark):
    width = 30
    line = "=" * width
    title = "CLASS SUMMARY"
    middle = title.center(width)

    print(line)
    print(middle)
    print(line)
    print(f"NUMBER OF STUDENTS: {num_students}")
    print(f"CLASS AVERAGE: {calculate_average:.2f}")
    print(f"HIGHEST SCORE: {max(student_scores)}")
    print(f"LOWEST SCORE: {min(student_scores)}")
    print(f"OVERALL GRADE: {class_grade}")
    print()
    print(class_remark)
    print(line)

num_students = get_number_of_students()
student_scores = []

for i in range(num_students):
    name, surname, score = input("Enter the student details (e.g. Justice Bishop 90): ").split()
    score = int(score)

    while score < 0 or score > 100:
        print("Invalid Score!")
        score = int(input("Enter the student score: "))

    grade = calculate_grade(score)
    remark = calculate_remark(grade)
    display_student_report(name, surname, score, grade, remark)

    student_scores.append(score)

average = calculate_average(student_scores, num_students)
class_grade = calculate_class_grade(average)
class_remark = calculate_class_remark(class_grade)
display_class_summary(num_students, student_scores, average, class_grade, class_remark)