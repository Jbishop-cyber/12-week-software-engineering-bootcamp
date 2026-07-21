# Exercise 1: search student

def search_student(students, name):

    found = False
    
    for i in students:
        if i == name:
            found = True
            return found
    return found

students = ["Justice", "Ada", "John"]

print(search_student(students, "Ada"))

# Excercise 2: find student index:

def find_student_index(students, name):
    
    for i in range (len(students)):
        if students[i] == name:
            print(f"The student is at index {i}")
            return i
    else:
        print("Student not found!")
        return -1
    
name = input("Enter the name of the student you are looking for: ")
students = ["Justice", "Jude", "Ayo", "John"]
index = find_student_index(students, name)

# Exercise 3: Count occurrences

def count_occurrences(numbers, n):

    count = 0

    for i in range (len(numbers)):
        if numbers[i] == n:
            count += 1

    if count == 0:
        print("Number not found!")

    return count

numbers = [2, 5, 2, 8, 2]
n = int(input("Enter a number: "))
result = count_occurrences(numbers, n)
print(f"{n} appears {result} times")
#print(result)

# Exercise 4: Largest number

def largest_number(n):

    if numbers == []:
        return None
    
    largest = numbers[0]
    
    for number in numbers:
        if number > largest:
            largest = number
    return largest

numbers = [12, 54, 26, 78, 103, 91]
print(largest_number(numbers))

# Exercise 5: find student

def student_exists(student_names, name):

    found = False
    
    for i in student_names:
        if i == name:
            found = True
            return found
    return found

student_names = ["Grace", "Victor", "Justice"]

print(student_exists(student_names, "Joe"))