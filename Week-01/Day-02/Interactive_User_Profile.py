"""Your program should ask the user for:

Full Name
Age
State
Country
Favourite Programming Language
Dream Job

Then display something like:

=================================
         USER PROFILE
=================================

Name: Jay
Age: 24
State: Abia
Country: Nigeria
Favourite Language: Python
Dream Job: Software Engineer

=================================
"""

name = input("What is your name? ")
age = input("How old are you? ")
state = input("What state are you from? ")
country = input("What country are you from? ")
favourite_language = input("What is your favourite programming language? ")
dream_job = input("What is your dream job? ")
line = "=" * 30

print(line)
print("         USER PROFILE         ")
print(line)
print(f"Name: {name}")
print(f"Age: {age}")
print(f"State: {state}")
print(f"Country: {country}")
print(f"Favourite Language: {favourite_language}")
print(f"Dream Job: {dream_job}")
print(line)
