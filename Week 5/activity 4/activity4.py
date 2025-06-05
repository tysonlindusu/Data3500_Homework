"""
Programming Activity 4

Write a Python program that takes a list of strings as input, where some strings might have leading or trailing spaces. Use list comprehension to remove these spaces from each string in the list.
"""

input_strings = ["  apple", "banana  ", "  cherry  ", " date", "fig "]

stripped_strings = [s.strip() for s in input_strings]

print(input_strings)
print(stripped_strings)