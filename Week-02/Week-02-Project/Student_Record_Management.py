def add_student(students):
    # Add student to the database
    prompt = "How many students do you want to add? "
    num_students = int(input(prompt))

    while num_students <= 0:
        print("Enter a valid Number")
        prompt = "How many students do you want to add? "
        num_students = int(input(prompt))
    
    for n in range(num_students):
        prompt = "Enter the student details i.e. (ID, name, surname, age, course): "
        student_ID, name, surname, age, course = input(prompt).split()
        age = int(age)
        while age <= 0 or age >= 50:
            print("Enter age between 1 - 50")
            age = int(input("Enter the student's age: "))

        prompt = "How many score do you want to enter for this student?"
        num_scores = int(input(prompt))
        scores = []

        while num_scores < 1:
            print("Invalid Number of Scores!")
            prompt = "How many scores do you want to enter for this student?"
            num_scores = int(input(prompt))

        for i in range(num_scores):
            score = int(input(f"Enter the score {i + 1}: "))
            while score < 0 or score > 100:
                print("Invalid Score!")
                score = int(input(f"Enter the score {i + 1}: "))
            scores.append(score)

        average = sum(scores) / len(scores)
        
        students[student_ID.lower()] = {"name": name.capitalize(), "surname": surname.capitalize(), "age": age, "course": course.capitalize(), "score": scores, "average": average}
        
    return students
    
def remove_student(students):
    # Remove student from the database
    while True:
        prompt = "Enter the student's ID to remove or type (exit) to cancel: "
        remove_ID = input(prompt).lower()
        
        if remove_ID == "exit":
            print("Returning to menu...")
            break
        
        if remove_ID.lower() in students:
            display_student(remove_ID, students[remove_ID])
            confirm = input("Are you sure you want to delete this student? (Y/N): ")
            
            if confirm.upper() == "Y":
                del students[remove_ID.lower()]
                print("Student removed successfully!")
                break
            else:
                print("Removal cancelled.")
        else:
            print("Student not found!")
            again = input("Do you want to try again (Y/N): ")
            if again.upper() == "N":
                break
        if again.upper() == "Y":
            continue
     
def search_student(students):
    # search student by ID or name
    while True:
        print("Search by: 1. ID  2. Name")
        choice = int(input("Choose an option: "))

        while choice <= 0 or choice > 2:
            print("Enter a valid Number")
            prompt = "Choose an option: "
            choice = int(input(prompt))
        
        search_term = input("Enter your search term: ").lower()
        
        if choice == 1:
            if search_term.lower() in students:
                display_student(search_term.lower(), students[search_term.lower()])
            else:
                print("Student not found!")
                again = input("Do you want to search again (Y/N): ")
                if again.upper() == "N":
                    print("OK")
                    break
                if again.upper() == "Y":
                    continue
        
        elif choice == 2:
            for student_ID, info in students.items():
                if info['name'].lower() == search_term.lower():
                    display_student(student_ID, info)
                    break 
            else:
                print("Student not found!")
                again = input("Do you want to search again (Y/N): ")
                if again.upper() == "N":
                    print("OK")
                    break
                if again.upper() == "Y":
                    continue
        
        search_again = input("Do you want to search again (Y/N): ")
        if search_again.upper() == "N":
            print("OK")
            break
        if search_again.upper() == "Y":
            continue
            
    return students

def display_student(student_ID, info):

    print("=" * 31)
    print(f"Student ID  : {student_ID.upper()}")
    print(f"Name        : {info['name']} {info['surname']}")
    print(f"Age         : {info['age']}")
    print(f"Course      : {info['course']}")
    print(f"Scores      : {', '.join(str(s) for s in info['score'])}")
    print(f"Average     : {info['average']}")
    print("=" * 31)


def display_all_students(students):
    """for student_ID, info in students.items():
        display_student(student_ID, info)"""

def main():
    students = {}
    
    while True:
        print("1. Add Student")
        print("2. Remove Student")
        print("3. Search Student")
        print("4. Display student statistics")
        print("5. Exit")
        
        choice = int(input("Choose an option: "))
        
        if choice == 1:
            add_student(students)
        elif choice == 2:
            remove_student(students)
        elif choice == 3:
            search_student(students)
        elif choice == 4:
            display_all_students(students)
        elif choice == 5:
            print("Exiting.....")
            break
        else:
            print("Invalid choice, try again.")
            
main()