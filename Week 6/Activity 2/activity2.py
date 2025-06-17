"""
Programming Activity 2

Write a program which asks the user to enter their address
Use the isalnum() function to verify the entered a valid address
- create a variable that stores the string address the user enters
- remove white space from the string
- use isalnum() on the string with no whitespace to verify all characters 
are numbers or letters
"""

# Ask the user to enter their address
address = input("Enter your address: ")

# Remove all spaces so we can check only letters and numbers
cleaned_address = address.replace(" ", "")

# Check if the cleaned address contains only letters and numbers
if cleaned_address.isalnum():
    print("Valid address.")
else:
    print("Invalid address. Only letters and numbers are allowed.")


"""
1. Write a function compare_strings(string1, string2) that compares two strings and returns "Equal" if they are equal (case-insensitive), "Different Lengths" if they have different lengths, and "Different Content" if they have the same length but different content.
"""

def compare_strings(string1, string2):
    # Check if the strings are equal when case is ignored
    if string1.lower() == string2.lower():
        return "Equal"
    
    # Check if the strings are different lengths
    if len(string1) != len(string2):
        return "Different Lengths"
    
    # If same length but different content
    return "Different Content"