"""
Programming Activity 3

Write a program which determines whether a child can sit in the front seat  of a car, using the following logic:
- if a child is 12 years old or older, they can sit in the front, regardless of weight.
- if a child is 11 years old, and over 90 pounds, they can sit in the front seat.
- if a child is under 11 years old, and over 100 pounds, they can sit in the front seat
- if a child does meet the criteria above they cannot sit in the front seat.
Your program will ask the user for a child's age and weight. Use Boolean variables to store the results of the criteria above. Use if statements and the Boolean variables created above to print a message to the user whether or not the child may sit in the front seat.
"""

# I think I'll use match to solve this because of the number of if statements, that's much cleaner

def determine_seat(age, weight):
    age = int(age)
    weight = int(weight)
    match age:
        case age if age >= 12:
            return True
        case age if age == 11 and weight >= 90:
            return True
        case age if age <= 11 and weight >= 100:
            return True
        case _:
            return False

can_sit_upfront = determine_seat(10,100)
if can_sit_upfront == True:
    print('You can sit up front')
else:
    print('You need to sit in the back to be safe!')