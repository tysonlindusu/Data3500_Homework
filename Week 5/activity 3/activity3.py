"""
Programming Activity 3

Write a Python program that creates a list of all even numbers from 2 to 100 using list comprehension.
"""

evens = [num for num in range(1,101) if num % 2 == 0]
print(evens)