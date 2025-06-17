"""
Programming Activity 1

Create a list with your 3 favorite colors. Display the message:
"My favorite colors are: blue, white, red" , 
but use the string join function to turn the list into a comma separated string.
- create a list with 3 favorite colors: ["blue", "white", "red"]
- create a string with value "My favorite colors are: "
- convert list to a comma separated string using join()
- concatenate the two strings and print the message
"""

# Make a list of your 3 favorite colors
favorite_colors = ["blue", "white", "grey"]

# Start building the message
message = "My favorite colors are: "

# Turn the list into a single string with commas in between
colors_string = ", ".join(favorite_colors)

# Combine the message with the color string and show it
full_message = message + colors_string
print(full_message)


#Challenge
"""
1. Write a Python program that takes a sentence as input and checks if it's a palindrome. Ignore spaces, so that phrases like "A man a plan a canal Panama" are considered palindromes.

2. Write a program that takes a sentence as input and reverses the words in the sentence without changing the order of words but removing any leading or trailing spaces.
"""

#1
# Ask the user for a sentence
sentence = input("Enter a sentence: ")

# Remove spaces and convert to lowercase for comparison
cleaned = sentence.replace(" ", "").lower()

# Check if the cleaned sentence reads the same backward
if cleaned == cleaned[::-1]:
    print("This is a palindrome.")
else:
    print("This is not a palindrome.")


#2
# Ask the user for a sentence
sentence = input("Enter a sentence: ")

# Remove leading and trailing spaces
trimmed = sentence.strip()

# Reverse the characters in each word while keeping word order
reversed_words = ' '.join(word[::-1] for word in trimmed.split())

print("Reversed words (characters only):", reversed_words)
