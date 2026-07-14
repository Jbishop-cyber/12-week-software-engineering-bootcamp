def get_number_of_students():
    num_students = int(input("How many students? "))

    while num_students <= 0:
        print("Invalid number of students")
        num_students = int(input("How many students? "))
    return num_students

def get_student_grade(num_students):
    student_name = []
    student_score = []

    for i in range(num_students):
        name, score = input("Enter student name and score (e.g. Jay 90): ").split()
        score = int(score)
        
        while score < 0 or score > 100:
            print("Invalid score")
            score = int(input("Enter student score: "))
        
        student_name.append(name)
        student_score.append(score)

    return student_name, student_score

def calculate_average(student_score, num_students):
    average = sum(student_score) / num_students
    return average

def display_report(average, student_score, num_students):
    width = 26
    line = "=" * width
    title = "CLASS REPORT"
    middle = title.center(width)

    print(line)
    print(title)
    print(line)
    print(f"Total Students: {num_students}")
    print(f"Highest Score: {max(student_score)}")
    print(f"Lowest Score: {min(student_score)}")
    print(f"Average Score: {average:.2f}")
    print(line)

num_students = get_number_of_students()
student_name, student_score = get_student_grade(num_students)
average = calculate_average(student_score, num_students)
display_report(average, student_score, num_students)
