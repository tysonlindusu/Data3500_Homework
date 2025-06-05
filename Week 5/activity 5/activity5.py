"""
Programming Activity 5

Write a Python program which asks the user their name.  
Store their name in a string variable. Use the Upper() function to make 
all of the letters in their name upper case. Then, print to the console: 
welcome, NAME ALLCAPS!.
 - using input get the user name
 - change the string to be all upper case
 - print to the console: "welcome, NAME ALLCAPS!" (adding an exclamation
"""

#input
name = input("What is your name? ")
#make it all caps
name_upper = name.upper()
#print the caps name
print(f"welcome, {name_upper}!")
