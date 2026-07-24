def add_student(students):
    prompt = "How many students do you want to add? "
    num_students = int(input(prompt))

    while num_students <= 0:
        print("Enter a valid Number")
        prompt = "How many students do you want to add? "
        num_students = int(input(prompt))
    
    for n in range(num_students):
        prompt = "Enter the student details i.e. (ID, name, surname, score, course): "
        student_ID, name, surname, score, course = input(prompt).split()
        score = int(score)
        students[student_ID.lower()] = {"name": name.capitalize(), "surname": surname.capitalize(), "score": score, "course": course.capitalize()}
    return students
    
def remove_student(students):
    while True:
        prompt = "Enter the student's ID to remove: "
        remove_ID = input(prompt)
        
        if remove_ID.lower() in students:
            del students[remove_ID.lower()]
            print("Student removed successfully!")
            break
        else:
            print("Student not found!")
            again = input("Do you want to try again (Y/N): ")
            if again.upper() == "N":
                break
        if again.upper() == "Y":
            continue
     
def search_student(students):
    while True:
        prompt = "Enter the student's ID:"
        search_ID = input(prompt)
        
        found = False
        
        if search_ID.lower() in students:
            info = students[search_ID.lower()]
            print(f"{search_ID.lower()}: {info['name']} {info['surname']} is a student")
            print()
            found = True
            break
        else:
            print("Student not found!")
            student_ID = input("Do you want to search again (Y/N): ")
            if student_ID.upper() == "N":
               print("OK")
               break
        if student_ID.upper() == "Y":
            continue

def display_students(students):
    width = 40
    line = "=" * width
    title = "STUDENTS DETAILS"
    middle = title.center(width)
    
    print(line)
    print(middle)
    print(line)
    for student_ID, info in students.items():
        print(f"{student_ID.upper()}: {info['name']} {info['surname']}, {info['score']}, {info['course']}")
    print(line)

def main():
    students = {}
    
    while True:
        print("1. Add Student")
        print("2. Remove Student")
        print("3. Search Student")
        print("4. View all students")
        print("5. Exit")
        
        choice = int(input("Choose an option: "))
        
        if choice == 1:
            add_student(students)
        elif choice == 2:
            remove_student(students)
        elif choice == 3:
            search_student(students)
        elif choice == 4:
            display_students(students)
        elif choice == 5:
            print("Exiting.....")
            break
        else:
            print("Invalid choice, try again.")
            
main()