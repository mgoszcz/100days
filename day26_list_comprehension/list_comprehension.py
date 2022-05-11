numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

# Print list of squared numbers
print([number **2 for number in numbers])

# Print list of even numbers
print([number for number in numbers if number%2 == 0])

"""
Instructions
Take a look inside file1.txt and file2.txt. They each contain a bunch of numbers, each number on a new line.

You are going to create a list called result which contains the numbers that are common in both files.

e.g. if file1.txt contained:

1
2
3
and file2.txt contained:

2
3
4
result = [2, 3]
IMPORTANT: The result should be a list that contains Integers, not Strings. Try to use List Comprehension instead of a Loop.

Example Output
[3, 6, 5, 33, 12, 7, 42, 13]
"""

with open('file1.txt', 'r') as file_handler:
    data1 = file_handler.readlines()

with open('file2.txt', 'r') as file_handler:
    data2 = file_handler.readlines()

print([int(number) for number in data1 if number in data2])
