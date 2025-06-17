"""
Programming Activity 6

Write a program that asks the user for two numbers. In a try statement, 
attempt to divide number 1 by number 2.  If number 2 is a 0, print a 
message in the except statement saying "Error, attempted to divide by zero"
- create two variables, inputted by the user
- in a  try: block attempt to divide num1 by num2
- in a except: block print a message indicating divide by zero error
- end program
"""

# Ask the user for two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Try to divide the two numbers
try:
    result = num1 / num2
    print(f"The result is: {result}")
except ZeroDivisionError:
    print("Error, attempted to divide by zero.")
