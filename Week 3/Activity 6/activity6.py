"""
Programming Activity 6

Update the function in activity one to have 3 variables: name (string),  age (int), favorite_color (string).  Create a new variable called welcome_message and assign it to the value "Welcome <name>, you are <age> years old, and <favorite_color> is your favorite color".  Return the variable welcome_message.
- Add two variables to your parameter list
- Concatenate those two variables in your welcome_message
- Return welcome_message just like you did in activity 2
- To test this, call welcome_fctn with 3 arguments
"""



def welcome_fctn(name, age, favorite_color):
    welcome_message = f"Welcome {name}, you are {age} years old, and {favorite_color} is your favorite color"
    return welcome_message

print(welcome_fctn("Bill", 23, "Green"))
