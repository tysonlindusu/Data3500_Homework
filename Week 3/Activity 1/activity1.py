"""
Programming Activity 1

Write a program which can tell if a 3 digit number is a palindrome. 
 - Create a variable, which stores user input. Prompt the user to enter a 3 digit number. 
 - Convert the user input into a integer (int). To get the first digit alone, floor division by 100. 
 - To get the 3rd digit alone, modulus by 10. 
 - Check if the first digit and 3rd digit are the same. 
 - If they are the same print("palindrome!!!!"). 
 - Else print("not palindrome!")
"""
# My approach does not convert to an integer -- I don't see the purpose of it here
# But if you need me to do it your way, I can do that.
# Using floor division and modulus to separate those numbers out is clever, but entirely unnecessary when you can keep it as a string
# and then just separate it into an array

incorrect_input = True

while incorrect_input:
    user_number = input('Please enter a 3 digit number: ')
    if len(user_number) != 3:
        print('You have not entered a valid 3 digit number')
    try:
        int(user_number)
    except ValueError:
        print('You did not input a number. Please try again.')
    incorrect_input = False

user_input_array = list(user_number)

if user_input_array[0] == user_input_array[2]:
    print('This is a palindrome')
else:
    print('This is not a palindrome')