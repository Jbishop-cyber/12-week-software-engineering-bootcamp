# Exercise 1 — Tuple Length

def tuple_length(data):
    count = 0
    for item in data:
        count += 1
    return count
print(tuple_length((10, 20, 30)))

# Exercise 2 — First and Last Item

def first_last(data):
    if data == ():    
        return None, None
    first, *others, last = data
    return first, last

print(first_last(("Justice", "Ada", "John")))

# Exercise 3 — Get Student Score

def get_score(student):
    return student["score"]

student = {
    "name": "Justice",
    "score": 95
}
print(get_score(student))

# Exercise 4 — Update Score

def update_score(student, new_score):

    student["score"] = new_score
    return student

student = {
    "name": "Justice",
    "score": 70
}
    
print(update_score(student, 90))

# Exercise 5: Add Course

def add_course(student, course):

    student["course"] = course
    return student

student = {
    "name": "Justice",
}
    
print(add_course(student, "Python"))

# Exercise 6 — Display Student Information

def display_student(student):

    for key, value in student.items():
        print(f"{key}: {value}")

student = {
    "name": "Justice",
    "score": 95,
    "grade": "A"
}

display_student(student)

# ⭐ Exercise 7 — Student Details

def student_details():

    width = 25
    line = "=" * 25
    title = "STUDENT DETAILS"
    middle = title.center(width)

    print(line)
    print(middle)
    print(line)
    for key, value in student.items():
        print(f"{key.capitalize()}: {value}")
    print(line)

student = {
    "name": "Justice",
    "score": 95,
    "grade": "A",
    "course": "Python"
}

student_details()