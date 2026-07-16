# Exercise 1 — Create Numbers

def create_numbers(n):
    
    numbers = []

    if n < 1:
        return []

    for i in range(1, n+1):
        numbers.append(i)
    
    return numbers
    
print(create_numbers(5))

# Exercise 2 — Even Numbers List
def even_numbers(n):

    evens = []

    if n < 2:
        return []

    for i in range(2, n+1, 2):
        evens.append(i)

    return evens

print(even_numbers(10))

# Exercise 3 — First and Last

def first_last(numbers):

    if numbers == []:
        return None, None

    first, *others, last = numbers
    return [first, last]

print(first_last([1, 2, 3, 4, 5]))

# Exercise 4 — Count Items

def count_items(items):

    count = 0

    for i in items:
        count += 1

    return count

print(count_items([10, 20, 30,]))
