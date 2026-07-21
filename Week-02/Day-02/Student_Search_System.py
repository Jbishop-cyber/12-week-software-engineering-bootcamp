
def number_of_students():
    
    num_students = int(input("How many student would be entered? "))
    
    while num_students <= 0:
        print("Enter a valid number!")
        num_students = int(input("How many student would be entered? "))
    return num_students

def store_student_names(num_students):

    if num_students < 1:
        return []
    
    student_names = []
    
    for i in range(num_students):
        name = input(f"Enter the name of student {i + 1}: ").strip()

        while not name:
            print("Enter a valid name: ")
            name = input(f"Enter the name of student {i + 1}: ").strip()
        
        student_names.append(name)
        
    return student_names
    
def first_and_last(students_names):

    if students_names == []:
        return None, None
    
    first, *others, last = students_names
    return first, last
    
def search_student(students_names):

    while True:
        name = input("Enter the name of student whose index you are looking for: ")
        found = False

        for i in range (len(students_names)):
            if students_names[i] == name:
                print(f"Student found at index {i}")
                found = True
                break
        if not found:
            print("Student not found!")
                
        search = input("Do you want to search again? (Y/N): ")
        if search.upper() == "N":
            break

num_students = number_of_students()
students_names = store_student_names(num_students)
first, last = first_and_last(students_names)

print(f"The total number of students entered is: {len(students_names)}")
print(f"Students: {students_names}")
print(f"First Student: {first}")
print(f"Last Student: {last}")

index = search_student(students_names)