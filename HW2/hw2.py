#problem 2.3 from the book

"""
2.3 (Fill in the missing code) Replace *** in the following code with a statement that will print a message like 'Congratulations! Your grade of 91 earns you an A in this course'. Your statement should print the value stored in the variable grade:
"""
print('===================== problem 2.3 =====================')
grade = 91

if grade >= 90:
    print(f'Congratulations! Your grade of {grade} earns you an A in this course')


#2.4

"""
2.4 (Arithmetic) For each of the arithmetic operators +, -, *, /, // and **, display the value of an expression with 27.5 as the left operand and 2 as the right operand.
"""

print('===================== problem 2.4 =====================')
print('addition: ',27.5 + 2, 'subtraction : ', 27.5 - 2, 'multiplication : ', 27.5 * 2, 'division: ', 27.5 / 2,'floor division: ',27.5 // 2, 'exponential: ', 27.5 ** 2)

#2.5
"""
2.5 (Circle Area, Diameter and Circumference) For a circle of radius 2, display the diameter, circumference and area. Use the value 3.14159 for π. Use the following formulas (r is the radius): diameter = 2r, 
circumference = 2πr and area = πr2. [In a later chapter, we’ll introduce Python’s math module which contains a higher-precision representation of π.]
"""

print('===================== problem 2.5 =====================')
radius = 2
pi = 3.14159
diameter = 2 * radius
circumference = 2 * pi * radius
area = pi * radius ** 2

print('diameter: ', diameter, 'circumference: ', circumference, 'area: ', area)

#2.6

"""
2.6 (Odd or Even) Use if statements to determine whether an integer is odd or even. [Hint: Use the remainder operator. An even number is a multiple of 2. Any multiple of 2 leaves a remainder of 0 when divided by 2.]
"""

print('===================== problem 2.6 =====================')

print('Enter a number:')
num = input()

try:
    num = int(num)
except ValueError:
    print('invalid input')

if num % 2 == 0:
    print('your number is even')
else:
    print('your number is odd')


#2.7

"""
2.7 (Multiples) Use if statements to determine whether 1024 is a multiple of 4 and whether 2 is a multiple of 10. (Hint: Use the remainder operator.)
"""

print('===================== problem 2.7 =====================')

if 1024 % 4 == 0:
    print('1024 is a multiple of 4')

if 10 % 2 == 0:
    print('2 is a multiple of 10')


#2.8

"""
2.8 (Table of Squares and Cubes) Write a script that calculates the squares and cubes of the numbers from 0 to 5. Print the resulting values in table format, as shown below. Use the tab escape sequence to achieve the three-column output.
"""

print('===================== problem 2.8 =====================')

for number in range (6):
    square = number ** 2
    cube = number ** 3
    print(f"{number}\t{square}\t{cube}")