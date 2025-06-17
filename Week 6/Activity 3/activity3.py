"""
Programming Activity 3

Write a program which asks the user for two numbers, stored in two variables num1 and num2. 
Generate a multiplication table for all integers 1 through num1 and 1 through num2. 
The bottom right entry in your table should have the product of num1 and num2. 
The table must be stored in a 2D list. 
The list must be created first with a nested for loop. 
Then, the table should be printed by another nested for loop iterating through the 2D list.
Steps:
- store the variables.
- create a list, and add empty lists to the list - however many your need from the variables above.
- append the values to the lists.
- use a nested for loop to iterate through the list and print the values.
"""

# Ask the user to enter two numbers
num1 = int(input("Enter the number of rows: "))
num2 = int(input("Enter the number of columns: "))

# Step 1: Create an empty 2D list (list of lists)
table = []

# Step 2: Use nested for loops to build the multiplication table
for i in range(1, num1 + 1):
    row = []  # Start a new row
    for j in range(1, num2 + 1):
        row.append(i * j)  # Add the product to the row
    table.append(row)  # Add the row to the table

# Step 3: Print the multiplication table
for row in table:
    for value in row:
        print(f"{value:4}", end="")  # Print each value with spacing
    print()  # Move to the next line after each row
