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

def update_student(student_names):
    index = int(input("What index do you want to change? "))

    while index >= len(student_names):  
        print("Invalid Index")
        index = int(input("What student index do you want to change? "))
    
    new_student = input("Enter the new student name: ")
    
    student_names[index] = new_student
        
    return student_names

def display_first_last(student_names):

    if student_names == []:
        return None, None

    first, *others, last = student_names
    return first, last
    
num_students = get_number_of_students()

student_names = students_names(num_students)

student_names = update_student(student_names)

first, last = display_first_last(student_names)

print(f"The total number of students is: {len(student_names)}")
print(student_names)
print(f"The first and last names are: {first} and {last}")

