def get_number_of_students():
    num_students = int(input("How many student would be entered?: "))

    while num_students <= 0:
        print("Please enter a vaild number!")
        num_students = int(input("How many students would be entered?: "))

    return num_students
    
def students_names(num_students):

    if num_students < 1:
        return []

    students_name = []

    for i in range(num_students):
        name = input(f"Enter name for student {i + 1}: ")

        students_name.append(name)

    return students_name

def display_first_last(student_names):

    if student_names == []:
        return None, None

    first, *others, last = student_names
    return first, last

def update_student(student_names):
    pass

num_students = get_number_of_students()

student_names = students_names(num_students)

print(student_names)

print(display_first_last(student_names))

