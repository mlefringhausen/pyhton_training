# generate_testdata() produces a list that contains the numbers
# from 1 to 1000. A randomly chosen duplicate number is inserted
# into the list, then the numbers are shuffled, so they are in
# random order.

# Task: Implement the find_duplicate function.

import random


def generate_testdata():
    numbers = range(1, 1001)
    duplicate = random.randint(1, 1000)
    numbers.append(duplicate)
    random.shuffle(numbers)
    return numbers, duplicate


def find_duplicate(numbers):
    x = set()
    for number in numbers:
        if number in x: return x
        x.add(number)


def find_duplicate_fast(numbers):
    x = []
    for number in numbers:
        if number in x: return x
        x.append(number)


def find_duplicates(numbers):
    x = []
    duplicates = []
    for number in numbers:
        if number in x: duplicates.append(number)
        x.append(number)
    return duplicates

numbers1 = [1, 2]
numbers2 = [0, 1, 3, 3]
numbers, duplicate = generate_testdata()

print "The real duplicate is", duplicate
print "Your algorithm found", find_duplicate(numbers)
print "Your algorithm should find number 1", find_duplicate(numbers1)
print "Your algorithm should find number 3", find_duplicate(numbers2)







