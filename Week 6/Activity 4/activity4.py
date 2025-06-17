"""
Programming Activity 4

Write a program which asks the user their age and favorite color.  
Store these values in a dictionary with keys "age" and "favorite_color".  
Also save the 2D list from the previous activity in the dictionary with the 
key "multiplication_table".
print all the values in the dictionary by iterating through the keys 
using a for loop.
"""

# Ask the user for their age and favorite color
age = input("Enter your age: ")
favorite_color = input("Enter your favorite color: ")

# Ask for dimensions to generate the multiplication table
num1 = int(input("Enter the number of rows for the multiplication table: "))
num2 = int(input("Enter the number of columns for the multiplication table: "))

# Create the multiplication table as a 2D list
multiplication_table = []
for i in range(1, num1 + 1):
    row = []
    for j in range(1, num2 + 1):
        row.append(i * j)
    multiplication_table.append(row)

# Create the dictionary and store the values
user_data = {
    "age": age,
    "favorite_color": favorite_color,
    "multiplication_table": multiplication_table
}

# Print each value in the dictionary by iterating through the keys
for key in user_data.keys():
    print(f"{key}: {user_data[key]}")
